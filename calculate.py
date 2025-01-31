import sys
import math

def process_input(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "<h3>Error: Invalid numeric input.</h3>"

    if a < 1:
        final_result = "<h3>Error: 'a' is too small (must be ≥ 1).</h3>"
    elif c < 0:
        final_result = "<h3>Error: 'c' must not be negative.</h3>"
    else:
        c_cubed = c ** 3
        if c_cubed > 1000:
            final_value = (math.sqrt(c_cubed) * 10)
        else:
            final_value = math.sqrt(c_cubed) / a

        final_value += b

        final_result = f"{final_value:.2f}"

        if b == 0:
            final_result += "<p>Note: 'b' is zero and does not affect the result.</p>"

    html_response = f"""
    <html>
    <head><title>Assignment 4</title></head>
    <body>
    <h1>Python Script Result</h1>
    <h3>Original Values:</h3>
    <p>A: {a}</p>
    <p>B: {b}</p>
    <p>C: {c}</p>
    <h3>Result:</h3>
    <p>{final_result}</p>
    </body>
    </html>
    """

    return html_response

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Content-type: text/html\n")
        print("<h3>Error: Missing input values.</h3>")
    else:
        a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
        print("Content-type: text/html\n")
        print(process_input(a, b, c))
