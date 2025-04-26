import socket

def send_post_request(pin):
    host = "127.0.0.1"
    port = 8888
    resource = "/verify"

    form_data = f"magicNumber={pin:03d}"
    request = f"""POST {resource} HTTP/1.1\r\nHost: {host}:{port}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(form_data)}\r\nConnection: close\r\n\r\n{form_data}"""

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)
        client_socket.connect((host, port))
        
        client_socket.sendall(request.encode())

        response = b""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data
        
        client_socket.close()

        return response.decode(errors="ignore")

    except socket.error as e:
        return f"Socket error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print(send_post_request(0))
