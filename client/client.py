"""
TODO: Client.py is the method for submitting images to the server
created in digits.py. The picutres containing the digits are housed in the
img directory contained in this directory. It posts to the /predict api of
the server created. 
"""

import sys
import requests


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    """Send image to server for prediction."""
    # TODO: Replace with code to send image to server
    ipAddress = f"http://{server_ip}:{server_port}{api_path}"
    files = {"img": open(image_path, "rb")}
    r = requests.post(ipAddress, files=files)
    return r.text
    # we want to post an HTTP request to the server


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    # TODO: Replace with prompt to user and call to get_img_prediction
    # server_ip = sys.argv[1]
    # server_port = sys.argv[2]
    img_path = "default"
    exitFlag = 1
    while exitFlag:
        img_path = input("Please enter the path to an image: ")
        if img_path != "exit":
            api_path = "/predict"
            print(f"Using server {server_ip}:{server_port}")
            text = get_img_prediction(server_ip, server_port, api_path, img_path)
            print(f"{text}\n")
        else:
            exitFlag = 0

    print("Goodbye!\n")


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
