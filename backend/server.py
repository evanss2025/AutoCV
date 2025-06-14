# flask code

from flask import Flask, jsonify, request, url_for, render_template, redirect, send_file
from flask_cors import CORS #helps with cross resources from connecting front to back end
from scraper import scraper_text
from pdf import PDF

#app instance
app = Flask(__name__)
CORS(app)

resume_sections = {
    'name': 'No Name',
    'contact': 'No Contact',
    'experience': [],
    'file-content': ""
}

print('flask running')
    
@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    print("submit form running")
    if request.method == 'POST':
        pdf = request.files['file']
        print("file:", pdf)
        content = scraper_text(pdf)

        resume_sections['contact'] = content.get('contact')
        resume_sections['name'] = content.get('name')
        resume_sections['file-content'] = content
        
        return content
    else:
        return "not post"

@app.route('/home', methods=['GET'])
def get_info():
    pdf = PDF(resume_sections['contact'], resume_sections['name'], 'experiences', 'classic')
    pdf.print_details()

    if request.method == 'GET':
        return jsonify({
            'contact': resume_sections['contact'],
            'name': resume_sections['name'],
            'experiences': resume_sections['experience'],
            'file-content': resume_sections['file-content'],
            })
    
def download(path):
    path = path
    return send_file(path, as_attachement=True)

if __name__ == '__main__':
    # run the app, debug=true only for development, remove in production
    app.run(debug=True, port=8080)
