"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that predicts 

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image
from io import BytesIO
from typing import Annotated
from fastapi import FastAPI, File

import numpy as np

model_path: str = "digits.keras"
# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!
file_object = open(model_path, "r")

# TODO: Create FastAPI App as global variable
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the server!"}

def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    gray_image = img.convert("L")
    resized_image = gray_image.resize((28,28))
    # TODO: convert image to numpy array of shape model expects
    image_array = np.array(resized_image)

    return image_array


# TODO: Define predict POST function
@app.post("/predict")
def get_request(img: Annotated[list[bytes], File()]) -> int:
    return {"file_sizes": [len(img)]}