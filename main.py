from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
        <!-- create your form here -->
            <form method="post">
                <div>
                    <label for="rot">Rotate by:</label>
                    <input type="text" name="rot" value="0">
                    <p class="error"></p>
                </div>
                <textarea type="text" name="text">{0}</textarea>
                <br>
                <input type="submit">
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods = ['POST'])
def encrypt():
    text = str(request.form.get('text'))
    rot = int(request.form.get('rot'))
    encrypted = rotate_string(text, rot)
    return form.format(encrypted)

app.run()