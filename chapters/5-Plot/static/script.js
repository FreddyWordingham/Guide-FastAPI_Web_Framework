/// Sample a point on the Mandelbrot set.
function sample() {
    const real = document.getElementById("real_input").value;
    const imag = document.getElementById("imag_input").value;

    const url = `http://localhost:8000/sample/${real}/${imag}`;
    window.location = url;
}

/// Sample a region of the Mandelbrot set.
/// Display the result as the page background image.
function plot() {
    const real = document.getElementById("real_input").value;
    const imag = document.getElementById("imag_input").value;
    const width = document.getElementById("width_input").value;
    const height = document.getElementById("height_input").value;
    const zoom = document.getElementById("zoom_input").value;
    const max_iter = document.getElementById("max_iter_input").value;

    const url = "http://localhost:8000/plot";
    const params = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            real: real,
            imag: imag,
            width: width,
            height: height,
            zoom: zoom,
            max_iter: max_iter,
        }),
    };

    fetch(url, params)
        .then((_response) => {
            document.body.style.backgroundImage = "url(/static/mandy.png?r=" + Math.random() + ")";
        })
        .catch((error) => {
            console.log(error);
        });
}

console.log("script.js loaded.");
