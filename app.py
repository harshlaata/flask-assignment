from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def api_data():
    try:
        with open('dataa.json') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

