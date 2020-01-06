from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.ssid.data))
        print(f'form submitted {form.ssid.data} {form.password.data}')
        return redirect('/index')
    return render_template('login.html', title='Connect', form=form)