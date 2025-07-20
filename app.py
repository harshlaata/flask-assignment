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

@app.route('/todo')
def todo():
    return render_template('todo.html')
from flask import request, redirect

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if not item_name or not item_description:
        return "Both fields are required", 400

    try:
        collection.insert_one({
            "item_name": item_name,
            "item_description": item_description
        })
        return redirect('/todo')  # Redirect back to the form
    except Exception as e:
        return f"Database error: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)

