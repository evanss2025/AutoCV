# flask code

from flask import Flask, jsonify, request, url_for, render_template, redirect
from flask_cors import CORS #helps with cross resources from connecting front to back end
from scraper import scraper_name

#app instance
app = Flask(__name__)
CORS(app)
    
@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    print("submit form running")
    if request.method == 'POST':
        f = request.files['file']
        print("file:", f)
        content = scraper_name(f)
        
        return content
    else:
        return "not post"

if __name__ == '__main__':
    # run the app, debug=true only for development, remove in production
    app.run(debug=True, port=8080)
