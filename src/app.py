from flask import Flask,render_template
import socket
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        executable_path = "../user-sync.py/dist/user-sync"
        result = subprocess.run([executable_path], capture_output=True, text=True)
        return render_template('index.html', hostname=host_name, ip=host_ip,result=result)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)