from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
   return "<p> Hello World ! </p>"

@app.route("/blog/<current_blog>")
def blog_page(current_blog):
   return f"You are on a blog called {escape(current_blog)}"

@app.route("/html_template/<query_param>")
def template(query_param):
   return render_template("hello.html", name=query_param)

if __name__ == "__main__":
   app.run(debug=True)