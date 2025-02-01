# Digits Client

Posts a request to the server to predict the number contained in an image.

## Usage
Ensure you are in a python venv. Note, it must be a different venv than the server venv.
After running requirements.txt, you need to run "python3 client.py <server ip> <server port>" 
We used 127.0.0.1 and 8000 because we were hosting on the same computer and 8000 is the default port

After that, you will be prompted to enter the path to an image. use img/X.png where X is the number
you would like to predict!

