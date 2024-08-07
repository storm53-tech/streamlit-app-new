from flask import Flask, jsonify
import requests

app = Flask(__name__)

CLOUD_FUNCTION_URL = 'https://REGION-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME'

@app.route('/latest-results', methods=['GET'])
def get_latest_results():
    try:
        response = requests.get(CLOUD_FUNCTION_URL)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

