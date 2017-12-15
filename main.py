from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/homepage", methods=["POST"])
def validate():
    
    username= request.form["username"]
    password= request.form["password"]
    verify= request.form["verify"]
    email= request.form["email"]
    
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    if username == "":
        username_error = "username cannot be blank"
    if password == "":
        password_error = "password cannot be blank"
    if verify == "":
        verify_error = "verify cannot be blank"

    for letter in username:
        if letter == " ":
            username_error = "This is an invalid entry"
    
    if len(username_error) <= 0 and (int(len(username)) < 3 or int(len(username)) > 20):
        username_error = "This is an invalid entry"
        username == ""
      
    for letter in password:
        if letter == " ":
            password_error = "This is an invalid entry" 

    if verify != password:
         verify_error = "Passwords did not match"
         verify == ""
    
    if int(len(email)) > 0:

        if int(len(email)) < 3 or int(len(email)) > 20:
            email_error = "This is an invalid entry"
            email == ""
    
        elif "@" not in email and "." not in email:
            email_error = "This is an invalid entry"
            email == ""
    if not username_error and not password_error and not verify_error and not email_error:
        username = str(username)
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template("index.html",username=username,email=email,username_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error)
@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username = username)
app.run()



