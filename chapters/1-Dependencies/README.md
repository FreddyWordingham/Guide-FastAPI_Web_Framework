# Dependencies

## Add dependencies

As we published our Mandelbrot package to PyPI, we can now install it using Poetry:

```bash
poetry add mandybrot
```

Alternatively, we could have installed it from a local directory:

```bash
poetry add mandybrot@../path/to/the/package
```

## Import

We can now import the `mandybrot` package into our [`main.py`](./api/main.py) file:

```python
import mandybrot as mandy
```

## Add route

We can now add a route to our application that calls the `point()` sampling function:

```python
@app.get("/sample/{real}/{imag}")
async def sample_point(real: float, imag: float):
    """
    Sample a complex point on the Mandelbrot set.
    """

    max_iters = 100
    result = mandy.sample.point(real, imag, max_iters)
    return f"({real}, {imag}) -> {result}"
```

## Try it

Make sure the application is running:

```bash
poetry run uvicorn api.main:app --reload --port 8000
```

And now we can visit a route like http://localhost:8000/sample/-0.761574/-0.0847596 to see the result:

![Sample point](./images/sample_point.png)

## Return

[Return to the top-level README](./../../README.md)
