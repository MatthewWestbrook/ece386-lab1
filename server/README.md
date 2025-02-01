# Digits Server

Accepts a POST request to predict the number contained in an image.

## Usage
Ensure you are in a python venv. Note, it must be a different venv than the client venv.
After running requirements.txt, you need to run "fastapi run digits.py" which will
host a server on the local ip of 127.0.0.1 and port 8000. This will then be used when
running the client.py file. 

