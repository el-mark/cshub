from flask import render_template,redirect,url_for,flash
from app import app
from app.forms import RegistrationForm, LoginForm

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('base.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Registration for {form.username.data} received','success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful', 'success')
        return redirect(url_for('home'))
    return render_template('login.html',form=form)

@app.route('/Content',methods=['GET','POST'])
def content():
    return render_template('course.html')

@app.route('/sw2',methods=['GET','POST'])
def sw2():
    return render_template('sw2.html')

@app.route('/aiml',methods=['GET','POST'])
def aiml():
    return render_template('aiml.html')

@app.route('/dsad',methods=['GET','POST'])
def dsad():
    return render_template('dsad.html')