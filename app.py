from flask import Flask, render_template

app = Flask(__name__)  # Use __name__ instead of name

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":  # Use __name__ for the main check
    app.run(host="0.0.0.0", port=5005, debug=True) # Enable debug mode for easier development
