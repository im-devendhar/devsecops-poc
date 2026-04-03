from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps POC"

@app.route("/exec")
def exec_cmd():
    cmd = request.args.get("cmd")
    return __import__('os').popen(cmd).read()

app.run(host="0.0.0.0", port=5000)
