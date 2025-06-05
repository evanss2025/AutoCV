# flask code

from flask import Flask, jsonify, request, url_for, render_template, redirect
from flask_cors import CORS #helps with cross resources from connecting front to back end

#app instance
app = Flask(__name__)
CORS(app)
    
@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    print("submit form running")
    if request.method == 'POST':
        link = request.form['link']
        
        return redirect(url_for("link", lnk=link))

    else:
        return "not post"

@app.route("/home")
def link():
    lnk = request.args.get("lnk")
    return f"{lnk}"


if __name__ == '__main__':
    # run the app, debug=true only for development, remove in production
    app.run(debug=True, port=8080)
