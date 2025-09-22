from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/info")
def info():
    headers = {}
    try:

        token = requests.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=1
        ).text
        headers = {"X-aws-ec2-metadata-token": token}
    except Exception:
        pass  
    try:
        response = requests.get("http://169.254.169.254/latest/meta-data/instance-id", headers=headers,timeout=1)
        response.raise_for_status()
        instance_id = response.text
    except Exception:
        instance_id = "not running on an EC2 instance"

    try:
        response = requests.get("http://169.254.169.254/latest/meta-data/placement/availability-zone", headers=headers,timeout=1)
        response.raise_for_status()
        availability_zone = response.text
    except Exception:
        availability_zone = "not running on an EC2 instance"

    return jsonify({
        "instance_id": instance_id,
        "availability_zone": availability_zone,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
