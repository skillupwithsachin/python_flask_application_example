from flask import Flask
app = Flask(__name__)  #WSGI - Web Server Gateway Interface
@app.route("/")
def hello():
    return "Welcome to SkillUpwithSachin!"; 

if __name__ == "__main__":
    app.run()
