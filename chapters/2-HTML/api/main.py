from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

import mandybrot as mandy

from . import settings


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def splashpage(request: Request):
    """
    Splash page for the API.
    """

    return settings.TEMPLATES.TemplateResponse("index.html", {"request": request})


@app.get("/sample/{real}/{imag}")
async def sample_point(real: float, imag: float):
    """
    Sample a complex point on the Mandelbrot set.
    """

    max_iters = 100
    result = mandy.sample.point(real, imag, max_iters)
    return f"({real}, {imag}) -> {result}"
