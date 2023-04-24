from flask import Flask , render_template , request


app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def home():
    
    
    return render_template("templates\index.index.html")






if __name__ == '__main__':
    
    app.run(port=1000,debug=True)
