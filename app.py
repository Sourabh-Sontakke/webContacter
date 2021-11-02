from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<string:page_name>")
def home(page_name):
    return render_template(page_name)

def write_file(data):
    email = data["email"]
    subject = data["subject"]
    content = data["content"]
    with open("database.csv", "a") as f:
        file = f.write(f"\n{email},{subject},{content}")
        

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_file(data)
        return redirect("/thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)