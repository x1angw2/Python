from flask import Flask


app = Flask(__name__)
@app.route('/index/',methods=['GET','POST'])
def index():
    return 'OK'
app.run()
