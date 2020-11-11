from . import app
from flask import render_template, request, session



@app.route('/', methods=["GET", "POST"])
def index():
    name = request.form.get("name")
    if name:
        session["name"]=name
    else:
        name = "Uživatel bez jména"
    title = 'Index'
    return render_template('base.html.j2', title=title, name=name)


@app.route('/info/')
def info():
    title = 'Info'
    return render_template('info.html.j2', title=title)

@app.route('/Květák')
def kvetak():
    title = 'Květák'
    return render_template('kvetak.html.j2', title=title)

@app.route('/Kapusta')
def kapusta():
    title = 'Kapusta'
    return render_template('kapusta.html.j2', title=title)

@app.route('/Banány')
def banany():
    title = 'Banány'
    return render_template('banany.html.j2', title=title)

@app.route('/Kalkulačka', methods=["GET", "POST"])
def formulky():
    label = request.form.get("text")
    if label:
        try:
            result = eval(label)
        except:
            result = "Error :)"
    else:
        result = ""
    title = 'Kalkulačka'
    return render_template('formula.html.j2', title=title, result=result)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html.j2')
