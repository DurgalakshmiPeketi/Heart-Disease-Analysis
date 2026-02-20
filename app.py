from flask import Flask, render_template

# Create Flask App
app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return render_template("index.html")

# Run the Server
if __name__ == "__main__":
    app.run(debug=True)
