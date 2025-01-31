"""
TODO: Insert what this program does here.
"""

import sys
import requests


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    """Send image to server for prediction."""
    # TODO: Replace with code to send image to server
    ipAddress = f"http://{server_ip}:{server_port}{api_path}"
    files = {'file': open(image_path,'rb')}
    r = requests.post(ipAddress,files=files,timeout = 1)
    return r.text
    # we want to post an HTTP request to the server



def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    # TODO: Replace with prompt to user and call to get_img_prediction
    ipAddress = sys.argv[1]
    port = sys.argv[2]

    while(input != "exit"):
        img_path = input("Please enter the path to an image: ")
        print(f"Using server {server_ip}:{server_port}")
        text = get_img_prediction(ipAddress,port,"/predict",img_path)
        print(f"The result of the prediction is: {text}\n")

    print("Goodbye!\n")
    


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
