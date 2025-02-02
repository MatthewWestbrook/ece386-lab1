# ece386-lab01

Serving handwritten digit inference with FastAPI.

See [USAFA ECE 386: AI Hardware Applications - Lab 1](https://usafa-ece.github.io/ece386-book/b1-prediction/lab-digits-api.html)

**GitHub Actions are enabled in this repository!** The workflow currently:

- Runs [Black](https://black.readthedocs.io/en/stable/index.html) format checker against client and server
- Runs [Pyright](https://microsoft.github.io/pyright/#/) type checker against client and server

## Writeup

*Answer the following questions. Strive to be articulate.*

### What strategies did you use to ensure that your client and server where communicating with the same schema?
We used a lot of print statements printing the size of our data to ensure they were talking using the same size variables. These print statements were SO useful because we had a ton of formatting issues where our img_to_numpy
function was not doing exactly what we needed. The print statements helped us find we were not inlcuding a batch size
and that needed to change. 

### In regard to preprocessing your digit images, how well do you think your server would scale to *any* picture of a digit?

### Does the client/server architecture make sense for this problem? Why or why not?

## Documentation
https://fastapi.tiangolo.com/tutorial/request-forms-and-files/#import-file-and-form
This helped us make the skeleton of the POST function! We copied a lot of the formatting things in class
after being shown this by C1C Mahajan. 

https://numpy.org/doc/2.1/reference/generated/numpy.vstack.html
This helped us prepare the data for interpretation by the server. We were really stuck getting some weird
errors and this alleviated a lot of the issues. 

https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
We were getting size errors on both the server and client side, this helped us fix that! Super easy once we
read the documentation!

https://numpy.org/doc/stable/reference/generated/numpy.argmax.html
https://chatgpt.com/share/679e92d1-9d44-8013-b18b-82c3a42e7e37
"I need help formatting a return value for a POST function. I think I need to use np.argmax.
I just did 'prediction = file_object.predict(np_img)' where np_img is a numpy image"
We were SO stuck with what to do here. Chat helped us understand what needed to happen in order to return
the correct thing. It makes total sense once we read it, but knowing that we needed that was the challenging
part!

C1C Alex White
Alex helped us with some silly mistakes such as IP address formatting mistakes in the client and feeling better
about what we returned in get_img_prediction function!

*Documentation statement. Pay special attention to the LLM policy.*
