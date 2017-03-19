from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('jMCQ-Creation-update.html', content="?",)


if (__name__ == '__main__'):
    app.run(debug=True)
