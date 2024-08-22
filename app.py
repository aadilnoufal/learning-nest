from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the user input from the form
    user_input = request.form['user_input']
    # Run the process_input.py script with the user input
    result = subprocess.check_output(['python3', 'process_input.py', user_input])
    # Decode the result from bytes to string and render the result page
    return render_template('result.html', result=result.decode('utf-8'))

if __name__ == "__main__":
    # Run the Flask app on port 5001
    app.run(host='0.0.0.0', port=5578)
