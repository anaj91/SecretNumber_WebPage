import random
from urllib import response
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secret_nr = request.cookies.get("secret_number")
    response = make_response(render_template("index.html"))
    if not secret_nr:
        new_secret_nr = random.randint(1, 30)
        response.set_cookie("secret_number", str(new_secret_nr))
    return response


@app.route("/rezultati", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))
    secret_nr = int(request.cookies.get("secret_number"))

    if guess == secret_nr:
        message = "Pravilno! Skrita številka je {0}".format(str(secret_nr))
        response = make_response(render_template("rezultati.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response
    elif guess > secret_nr:
        message = "Tvoje število ni pravilno. Poskusi z manjšim številom."
        return render_template("rezultati.html", message=message)
    elif guess < secret_nr:
        message = "Tvoje število ni pravilno. Poskusi z večjim številom."
        return render_template("rezultati.html", message=message)


if __name__ == '__main__':
    app.run(use_reloader=True)