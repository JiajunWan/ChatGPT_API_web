from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_text = request.form.get("input_text")
        # Add your code here to make an HTTP request and get the response
        # For example, using the requests library:
        # response = requests.get("https://example.com/api/search?q=" + input_text)
        # result = response.text

        result = "Example response"

        return result
    return """
        <form method="post">
            <input type="text" name="input_text">
            <input type="submit" value="Submit">
        </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0")