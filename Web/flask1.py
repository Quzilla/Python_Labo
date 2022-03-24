from flask import Flask, render_template, request
app = Flask(__name__, )

@app.route("/")
def hello_world():
    thing = request.args.get('thing')
    height = request.args.get('height')
    color = request.args.get('color')
    return render_template('index.html', thing=thing, height=height, color=color)

app.run(host='localhost',port=4000, debug=True)