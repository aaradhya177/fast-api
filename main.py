# Import the FastAPI class from the fastapi package.
from fastapi import FastAPI

# Create a FastAPI application object and store it in the variable named app.
app = FastAPI()

# Tell FastAPI to run the home function when someone visits the root URL: "/".
@app.get("/")
def home():
    # Send this dictionary back as the API response; FastAPI converts it to JSON.
    return {"message": "my first api is working"}

# Tell FastAPI to run the hi function when someone visits the "/hi" URL.
@app.get("/hi")
def hi():
    # Send a simple JSON response with the message "hi".
    return {"message": "hi"}

# Tell FastAPI to run the about function when someone visits the "/about" URL.
@app.get("/about")
def about():
    # Send information about this API, including its name/purpose and version.
    return {"message": "loan risk model", "version": "1.0"}

@app.get("/number")
def number():
    return {"number": 242}
