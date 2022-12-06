from flask import Flask,render_template
import os

app = Flask(__name__)
picFolder = os.path.join('static', 'pics')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def hello_world():
   pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.jpeg')
   return render_template('index.html',user_image=pic1)
@app.route('/sitemap.xml')
def sitemap():
   sitemap_xml = render_template('sitemap.xml')
   response = make_response(sitemap_xml)
   response.headers['Content-Type'] = 'application/xml'
   return response
   

if __name__ == "__main__":
   app.run()
