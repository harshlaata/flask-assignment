from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

# Replace this with your actual MongoDB connection string
client = MongoClient("mongodb+srv://iamravisharma1:12345@learnmongo.igevijc.mongodb.net/?retryWrites=true&w=majority&appName=learnmongo")
db = client["flaskapp"]
collection = db["flaskapp"]

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')

        if not name or not age or not city:
            error = "All fields are required!"
            return render_template('form.html', error=error)

        # Try inserting into MongoDB
        try:
            collection.insert_one({
                "name": name,
                "age": int(age),  # Optional: convert age to integer
                "city": city
            })
            return redirect(url_for('form_submitted'))
        except PyMongoError as e:
            error = f"Database error: {e}"
            return render_template('form.html', error=error)

    return render_template('form.html')

@app.route('/formsubmitted')
def form_submitted():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)

