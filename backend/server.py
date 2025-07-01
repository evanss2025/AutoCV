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
    'summary': 'No Summary',
    'experiences': 'No Experience',
    'education': 'No Education',
    'skills': 'No Skills',
    'languages': 'No Languages',
    'certifications': 'No Certifications',
    'awards': 'No Awards',
    'file-content': ""
}
    
@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        pdf = request.files['file']
        content = scraper_text(pdf)

        resume_sections['contact'] = content.get('contact')
        resume_sections['name'] = content.get('name')
        resume_sections['summary'] = content.get('summary')
        resume_sections['experiences'] = content.get('experiences')
        resume_sections['education'] = content.get('education')
        resume_sections['skills'] = content.get('skills')
        resume_sections['languages'] = content.get('languages')
        resume_sections['certifications'] = content.get('certifications')
        resume_sections['awards'] = content.get('awards')
        resume_sections['file-content'] = content
        
        return content
    else:
        return "not post"

@app.route('/home', methods=['GET'])
def get_info():
    if request.method == 'GET':
        return jsonify({
            'contact': resume_sections['contact'],
            'name': resume_sections['name'],
            'summary': resume_sections['summary'],
            'experiences': resume_sections['experiences'],
            'education': resume_sections['education'],
            'skills': resume_sections['skills'],
            'languages': resume_sections['languages'],
            'certifications': resume_sections['certifications'],
            'awards': resume_sections['awards'],
            'file-content': resume_sections['file-content'],
            })
    
#downloading route 
@app.route('/download/<type>', methods=['GET'])
def download(type):
    pdf = PDF (
        name = resume_sections['name'],
        contact = resume_sections['contact'],
        summary = resume_sections['summary'],
        experiences = resume_sections['experiences'],
        education = resume_sections['education'],
        skills = resume_sections['skills'],
        languages = resume_sections['languages'],
        certifications = resume_sections['certifications'],
        awards =  resume_sections['awards'],
        type = type
    )
    PDF_buffer = pdf.create_pdf()

    # pdf.print_details()

    return send_file (
        PDF_buffer,
        as_attachment = True,
        download_name = f"{type}_resume.pdf",
        mimetype = "application/pdf"
    )


if __name__ == '__main__':
    # run the app, debug=true only for development, remove in production
    app.run(host="0.0.0.0", port=8080)
