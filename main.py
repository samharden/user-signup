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
    if len(pw) > 4 and pw == pw2 and '@' in em and len(un) > 3 and len(un)<20:
        return render_template('success.html', text = un)
    elif pw == pw2 and '@' in em and len(un) < 3:
        un_error = 'Username must be at least 4 characters'
    elif pw != pw2 and '@' not in em:
        pw_result = 'Passwords do not match'
        email_result = 'Not a valid email address!'
    elif '@' not in em:
        email_result = 'Not a valid email address!'
        pw_result = ''
    elif '@' in em and pw == pw2 and len(un)>3:
        return redirect('success.html')


    return render_template(
                            'home.html',
                            name_error = un_error,
                            password1_error = pw_result,
                            password2_error = pw_result,
                            email_error = email_result
                            )
@app.route("/success")
def success():
    return render_template('success.html')


app.run()
