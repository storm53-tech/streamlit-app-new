from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace with your actual Cloud Function URL
cloud_function_url = "https://us-central1-aclgrafts-lindyscore-430915.cloudfunctions.net/get_lindy_scores"

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the ACL Grafts Lindy Score API!"

@app.route('/latest-results', methods=['GET'])
def get_latest_results():
    try:
        # For production, do not disable SSL verification
        response = requests.get(cloud_function_url, verify=True)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
    except requests.exceptions.SSLError:
        # For development, you can disable SSL verification temporarily
        response = requests.get(cloud_function_url, verify=False)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

