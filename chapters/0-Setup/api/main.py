from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def splashpage():
    """
    Splash page for the API.
    """

    return f"Hello, World!"
