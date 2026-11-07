from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>DevOps CI/CD Project</title>
    </head>
    <body style="background:#111827;color:#38bdf8;text-align:center;padding:50px;">
        <h1>Welcome to Rajesh Void!</h1>
        <h2>AWS End-to-End CI/CD Deployment</h2>
        <p>Application deployed successfully using Jenkins and Docker.</p>
        <p>Hosted on Amazon EC2.</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "devops-demo-app"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
