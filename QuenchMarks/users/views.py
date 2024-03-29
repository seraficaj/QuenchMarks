from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from QuenchMarks import db
from QuenchMarks.models import User, Bottle, user_favorites
from QuenchMarks.users.forms import RegistrationForm,LoginForm,UpdateUserForm

users = Blueprint('users',__name__)

# register
@users.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))

    return render_template('register.html',form=form)



# login
@users.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):

            login_user(user)
            flash('Logged in successfully!')

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html',form=form)


# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))


# account (update UserForm)
@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():

    form = UpdateUserForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', form=form)

@users.route("/<username>")
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user_profile.html',user=user)

# favorite a bottle
@users.route("/<int:user_id>/add_fave/<int:bottle_id>", methods=['GET','POST'])
@login_required
def add_fave(user_id, bottle_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    user.favorites.append(Bottle.query.get(bottle_id))
    db.session.commit()
    print(user.favorites)
    return redirect(url_for('bottles.bottle_detail', id=bottle_id))

# UNfavorite a bottle
@users.route("/<int:user_id>/remove_fave/<int:bottle_id>", methods=['GET','POST'])
@login_required
def remove_fave(user_id, bottle_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    user.favorites.remove(Bottle.query.get(bottle_id))
    db.session.commit()
    return redirect(url_for('bottles.bottle_detail', id=bottle_id))