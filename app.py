from flask import render_template, url_for, redirect, make_response, flash
from flask_login import login_user, LoginManager, login_required, logout_user, current_user

from forms import RegisterForm, LoginForm, UpdateForm, ContactForm
from db_tables import User, Message
from create_app import create_app
from encryption import encrypt, decrypt

app, db, bcrypt = create_app()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/home")
@app.route("/")
@login_required
def index():
    if current_user.is_authenticated:
        return render_template("index.html")
    else:
        return render_template("login.html")


@app.route("/library")
@login_required
def library():
    return render_template("library.html")


@app.route("/pricing")
@login_required
def pricing():
    return render_template("pricing.html")


@app.route("/contact", methods=['GET', 'POST'])
@login_required
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        file = form.file.data
        if file:
            with file.stream as f:
                file_text = f.read().decode("utf-8")

            new_message = Message()
            new_message.user_id = current_user.get_id()
            new_message.message = file_text
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template("contact.html", form=form)


@app.route("/sitemap")
@login_required
def sitemap():
    return render_template("sitemap.html")


@app.route("/profile")
@login_required
def profile():
    user_info = {
        'email': current_user.email,
        'fullname': current_user.fullname
    }
    return render_template("profile.html", user=user_info)


@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email is already taken. Please choose a different one.', 'error')
            return render_template('registration.html', form=form)
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User()
        new_user.role_id = 2
        new_user.email = form.email.data
        new_user.password = hashed_password
        new_user.fullname = form.fullname.data
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)

                user_id = current_user.get_id()
                response = make_response(redirect(url_for('index')))
                response.set_cookie('session_id', user_id)

                return response
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/update', methods=['GET', 'POST'])
@login_required
def update_account():
    form = UpdateForm()
    if form.validate_on_submit():
        user_to_modify = User.query.filter_by(id=current_user.get_id()).first()
        if user_to_modify:
            user_to_modify.fullname = form.fullname.data
            db.session.commit()
            return redirect(url_for('profile'))
    return render_template('update_account.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
@login_required
def delete_account():
    user_to_delete = User.query.filter_by(id=current_user.get_id()).first()
    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
