from flask import Flask, request, render_template, redirect

# from forms import form

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():

    return render_template(
                            'home.html',
                            name_error = '',
                            password1_error = '',
                            password2_error = '',
                            email_error = ''
                            )


@app.route("/", methods=["POST"])
def log_in():

    un = str(request.form["user_name"])
    pw = str(request.form["password"])
    pw2 = str(request.form["password2"])
    em = str(request.form['email'])
    un_error = ''
    pw_result = ''
    email_result = ''
    if len(pw) > 4 and pw == pw2 and len(em) == 0 and len(un) > 3 and len(un)<20:
        return render_template('success.html', text = un)
    elif pw == pw2 and len(un) < 3:
        un_error = 'Username must be at least 4 characters'
    elif pw != pw2 and len(em) > 0 and '@' not in em:
        pw_result = 'Passwords do not match'
        email_result = 'Not a valid email address!'
    elif pw != pw2 and len(pw) <= 4:
        pw_result = 'Passwords do not match and are too short!'
    elif pw != pw2:
        pw_result = 'Passwords do not match'
    elif len(pw) <= 4:
        pw_result = 'Password must be at least 5 characters!'
    elif len(em) > 0 and '@' not in em:
        email_result = 'Not a valid email address!'


    return render_template(
                            'home.html',
                            un = un,
                            email= em,
                            name_error = un_error,
                            password1_error = pw_result,
                            password2_error = pw_result,
                            email_error = email_result
                            )
@app.route("/success")
def success():
    return render_template('success.html')


app.run()
