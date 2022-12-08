from flask import Flask
from flask import request, Response, render_template, redirect, url_for, send_file
# import get_image
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session

#Change this path when running on your system if needed. Database is in the current working directory.
engine = sqlalchemy.create_engine('sqlite:///cve')

app = Flask(__name__)

# disable cache
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/styleGuide")
def styles():
    return render_template("styleGuide.html")

@app.route("/vendors")
def vendors():
    return render_template("byVendor.html")

@app.route("/products")
def products():
    return render_template("byProduct.html")

@app.route("/main1")
def main1():
    return render_template("main1.html")

@app.route("/main2")
def main2():
    return render_template("main2.html")

@app.route("/not-allowed")
def notAllowed():
    return render_template("not-allowed.html")

@app.route("/sample")
def sample():
    return render_template("sample.html")

@app.route("/product-search")
def productSearch():
    return render_template("product-search.html")

@app.route("/searchquery")
def searchquery():
    return render_template("searchquery.html")


@app.route("/apple")
def apple():
    return render_template("apple.html")

@app.route("/appache")
def appache():
    return render_template("appache.html")

@app.route("/adobe")
def adobe():
    return render_template("adobe.html")

@app.route("/oracle")
def oracle():
    return render_template("oracle.html")

@app.route("/microsoft")
def microsoft():
    return render_template("microsoft.html")

@app.route("/linux")
def linux():
    return render_template("linux.html")

@app.route("/ibn")
def ibn():
    return render_template("ibn.html")

@app.route("/google")
def google():
    return render_template("google.html")

@app.route("/devian")
def devian():
    return render_template("devian.html")

@app.route("/api/v1/query", methods=["GET", "POST"])
def query():
    out = ""
    if request.method == "POST":
        if request.form["query"]:
            query = request.form["query"]
            Session = scoped_session(sessionmaker(bind=engine))
            s = Session()
            try:
                # ooooo scaryyy! FIXME: sanitize/escape user input!!!
                print(query)
                result = s.execute(query)
                print(result)
                # iterate through results
                for item in result:
                    #print(item)
                    out = out + str(item) + " \n"
                print("Query Successful.")
                return out

            except:
                print("Query Failed.")
                return "Invalid SQL Statement or SQL error."
        else:
            return "No Query."

    else:
        return ">:("



if __name__ == '__main__':
    Flask.run(app, port="7777", debug=True)
