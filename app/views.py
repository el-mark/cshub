from flask import render_template,redirect,url_for,flash,request
from app import app,bcrypt,db
from app.forms import RegistrationForm, LoginForm,UpdateAccountForm
from app.models import User, Link, Like
from flask_login import login_user,current_user, logout_user, login_required

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('base.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email= form.email.data , password = hashed_pw)
        db.session.add(user)
        db.session.commit()

        flash(f"Your account has been created, you can now log in",'success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember= form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home')) #if i went to the login page while trying to access another page, this will make sure to redirect me to that page if i logged in successfully
        else:
            flash('Login unsuccessful, please check email and password', 'danger')
    return render_template('login.html',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account info has been updated','success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file )
    return render_template('account.html', title='Account', image_file=image_file, form=form)

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

@app.route('/articles',methods=['GET'])
@login_required
def articles():
    return render_template('array_vs_list.html')

@app.route('/links',methods=['GET'])
def links():
    links = Link.query.all()
    return render_template('links.html', links=links, like=Like)

@app.route('/like_link/<int:link_id>',methods=['GET'])
def like_link(link_id):
    like = Like(user_id=current_user.id,link_id=link_id)
    db.session.add(like)
    db.session.commit()
    
    return redirect(url_for('links'))

@app.route('/unlike_link/<int:link_id>',methods=['GET'])
def unlike_link(link_id):
    like = Like.query.filter_by(user_id=current_user.id, link_id=link_id).first()
    db.session.delete(like)
    db.session.commit()
    
    return redirect(url_for('links'))
