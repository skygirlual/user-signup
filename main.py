from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form["username"]
    password = request.form["password"]
    passwordV = request.form["passwordV"]
    email=request.form["email"]

  #  return render_template("user-signup.html", username=username)

    checklist = [username, password, passwordV, email]

    user_error = ""
    password_error = ""
    passwordV_error = ""
    email_error = ""

    for i in checklist:
        if len(username) < 3 or len(username) > 20:
            user_error = "Invalid user name"
            return render_template('user-signup.html', username = username, user_error = user_error)
#        else: 
#            return render_template('welcome.html', username = username)

    #for i in checklist: #go through password 1 criteria
        if len(password) < 3 or len(password) > 20 or " " in password:
            password_error = "Password must contain 3 to 20 characters and no spaces "
            return render_template('user-signup.html', username = username, password= password, passwordV= passwordV, password_error = password_error)
 #       else: 
 #           return render_template('welcome.html', username = username)

    #for i in checklist:		
        if password != passwordV:
            passwordV_error = "Password does not match"
            return render_template('user-signup.html', username = username, password= password, passwordV = passwordV, passwordV_error = passwordV_error)
  #      else: # else render user-signup html, using error variables
  #          return render_template('welcome.html', username = username)

    #email paramaters 
    #for i in checklist: #go through email criteria
        
        if "." not in email and len(email) !=0:
            email_error = "email must contain exactly 1 . symbol "
            return render_template('user-signup.html', username = username, password= password, passwordV = passwordV,email= email, email_error = email_error)
        if "@" not in email and len(email) !=0:
            email_error = "email must contain 1 @ symbol "
            return render_template('user-signup.html', username = username, password= password, passwordV = passwordV,email= email, email_error = email_error)
        if " " in email and len(email) !=0:
            email_error = "email must not contain any spaces "
            return render_template('user-signup.html', username = username, password= password, passwordV = passwordV,email= email, email_error = email_error)
        if ((len(email) < 3 or len(email) > 20) and len(email) !=0):
            email_error = "email must contain 3 to 20 characters "
            return render_template('user-signup.html', username = username, password= password, passwordV = passwordV,email= email, email_error = email_error)
   # else: 
   #         return render_template('welcome.html', username = username)


    if not user_error and not password_error and not passwordV_error and not email_error:
        return render_template('welcome.html', username = username)

#    return "Hello"
#@app.route("/welcome")
#def login_compete():
#	return "<h1>Hello {{username}}<h1>"

@app.route("/")
def hello():
    encoded_error =  request.args.get("error")
    return render_template("user-signup.html", error=encoded_error and cgi.escape(encoded_error,quote=True))

app.run()
