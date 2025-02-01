"""
TODO: 
This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.

Digits.py is a FastAPI app that predicts the number contained
in a 28x28 black and white image. It accepts a POST request 
from the cleint.py file. It uses the digits.keras model
to make these predictions. The model was made by training on
the NIST digits dataset. 
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image
from io import BytesIO
from typing import Annotated, List
from fastapi import FastAPI, File, UploadFile

import numpy as np

model_path: str = "digits.keras"
# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!
file_object = load_model(model_path)

# TODO: Create FastAPI App as global variable
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the server! Nice to see you"}


def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    gray_image = img.convert("L")
    resized_image = gray_image.resize((28, 28))
    # TODO: convert image to numpy array of shape model expects
    image_array = np.array(resized_image)

    # we were getting some issues with batch size, so I manually added it
    image_array = image_array.reshape((1, 28, 28))

    return image_array


# # TODO: Define predict POST function
# @app.post("/predict")
# async def get_request(img: Annotated[list[bytes], File()]):
#     prediction = file_object.predict(img)
#     return {"image prediction:": prediction}


# TODO: Define predict POST function
@app.post("/predict")
async def get_request(img: Annotated[List[bytes], File()]) -> dict:
    np_img = np.vstack([image_to_np(image) for image in img])

    print(f"initial batch shape: {np_img.shape}")
    prediction = file_object.predict(np_img)

    # this came from chat gpt - documented
    predicted_label = np.argmax(prediction, axis=1).tolist()

    return {"image prediction:": predicted_label}
