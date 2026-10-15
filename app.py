
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSE30040 CI/CD Lab</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 60px;
                background: #eef4ff;
            }
            .card {
                background: white;
                max-width: 650px;
                margin: auto;
                padding: 35px;
                border-radius: 16px;
                box-shadow: 0 4px 18px #0002;
            }
            h1 { color: #174ea6; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>CSE30040 Cloud Computing and DevOps</h1>
            <h2>Experiment 5: CI/CD with Jenkins</h2>
            <p>Flask application deployed using Docker on AWS EC2.</p>
            <p>Status: Application is running successfully!</p>
            <p>Version: 1</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
