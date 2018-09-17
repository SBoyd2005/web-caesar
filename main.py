from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


form="""
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <form method= "post">
    <textarea name="text">
    <input name="rot" value= 0>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/rotate")
def rotate():
    app.run()