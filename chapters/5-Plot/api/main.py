from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import mandybrot as mandy

from . import settings


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


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


class PlotInput(BaseModel):
    real: float
    imag: float
    width: int
    height: int
    zoom: float
    max_iter: int


@app.post("/plot")
async def plot(input: PlotInput):
    """
    Plot a region of the Mandelbrot set.
    """

    data = mandy.sample.area(
        input.real, input.imag, input.width, input.height, input.zoom, input.max_iter
    )
    cols = mandy.colour.image(data, input.max_iter, mandy.colour.jet_map)
    img = mandy.colour.encode(cols)
    img.save("static/mandy.png")

    return "Complete."
