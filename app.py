from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def hashing(pwd, num_char):
    # кодирование
    byte_str = pwd.encode()
    # хеширование
    hash_str = hashlib.sha256(byte_str)
    # преобразование в строку
    if num_char == '-':
        return hash_str.hexdigest()
    else:
        return hash_str.hexdigest()[:int(num_char)]


@app.route("/", methods=["GET", "POST"])
def index_page():
    msg = ""
    if request.method == "POST":
        site_name = request.form.get("site")
        pwd = request.form.get("pwd")
        num_char = request.form.get("num")

        msg = hashing(site_name + pwd, num_char)

    return render_template("index.html", message=msg)

@app.route("/contact")
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
