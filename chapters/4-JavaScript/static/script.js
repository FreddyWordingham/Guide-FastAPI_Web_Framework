/// Sample a point on the Mandelbrot set.
function sample() {
    const real = document.getElementById("real_input").value;
    const imag = document.getElementById("imag_input").value;

    const url = `http://localhost:8000/sample/${real}/${imag}`;
    window.location = url;
}

console.log("script.js loaded.");
