from . import app
from flask import render_template, request, session, redirect, url_for, g
from os import urandom

@app.route('/')
def index():
    if g.user:
        title = 'Index'
        return render_template('base.html.j2', title=title, user=session['user'])
    return redirect(url_for('login'))

@app.route('/info/')
def info():
    if g.user:
        title = 'Info'
        return render_template('info.html.j2', title=title)
    return redirect(url_for('login'))

@app.route('/Květák')
def kvetak():
    if g.user:
        title = 'Květák'
        return render_template('kvetak.html.j2', title=title)
    return redirect(url_for('login'))

@app.route('/Kapusta')
def kapusta():
    if g.user:
        title = 'Kapusta'
        return render_template('kapusta.html.j2', title=title)
    return redirect(url_for('login'))

@app.route('/Banány')
def banany():
    if g.user:
        title = 'Banány'
        return render_template('banany.html.j2', title=title)
    return redirect(url_for('login'))

@app.route('/Kalkulačka', methods=["GET", "POST"])
def formulky():
    if g.user:
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
    return redirect(url_for('login'))


app.secret_key = urandom(24)

@app.route('/login', methods=["GET", "POST"])
def login():
    wrongpassword = ""
    if request.method == "POST":
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect(url_for('index'))
        wrongpassword = "No zkus to znova 😉"

    title = 'login'
    return render_template('login.html.j2', title=title, wrongpassword=wrongpassword)

@app.before_request
def before_request():
    g.user = None

    if 'user' in session:
        g.user = session['user']

@app.route('/')
def dropsession():
    session.pop('user', None)
    return render_template('login.html.j2')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html.j2')
