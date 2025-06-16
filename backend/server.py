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
    'title': 'No Title',
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
        resume_sections['title'] = content.get('title')
        resume_sections['file-content'] = content
        
        return content
    else:
        return "not post"

@app.route('/home', methods=['GET'])
def get_info():
    pdf = PDF(resume_sections['contact'], resume_sections['name'], resume_sections['title'], 'experiences', 'classic')
    pdf.print_details()

    if request.method == 'GET':
        return jsonify({
            'contact': resume_sections['contact'],
            'name': resume_sections['name'],
            'title': resume_sections['title'],
            'experiences': resume_sections['experience'],
            'file-content': resume_sections['file-content'],
            })
    
#downloading route 
@app.route('/download/<type>', methods=['GET'])
def download(type):
    pdf = PDF (
        name = resume_sections['name'],
        title = resume_sections['title'],
        contact = resume_sections['contact'],
        experiences = resume_sections['experience'],
        type = type
    )
    PDF_buffer = pdf.create_pdf()

    return send_file (
        PDF_buffer,
        as_attachment = True,
        download_name = f"{type}_resume.pdf",
        mimetype = "application/pdf"
    )


if __name__ == '__main__':
    # run the app, debug=true only for development, remove in production
    app.run(debug=True, port=8080)
