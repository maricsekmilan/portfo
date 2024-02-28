from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    try:
        with open('database.txt', 'a+') as database:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            file = database.write(f'\n{email},{subject},{message}')
    except Exception as e:
        print(f"Hiba történt a fájl írása közben: {str(e)}")

def write_to_csv(data):
    try:
        with open('database.csv', mode='w') as database2:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.write(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])
    except Exception as e:
        print(f"Hiba történt a fájl írása közben: {str(e)}")

@app.route("/submit_form", methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('/thankyou.html')
        except Exception as a:
            print(a)

    


