from fastapi import FastAPI

import mandybrot as mandy


app = FastAPI()


@app.get("/")
async def splashpage():
    """
    Splash page for the API.
    """

    return f"Hello, World!"


@app.get("/sample/{real}/{imag}")
async def sample_point(real: float, imag: float):
    """
    Sample a complex point on the Mandelbrot set.
    """

    max_iters = 100
    result = mandy.sample.point(real, imag, max_iters)
    return f"({real}, {imag}) -> {result}"
