from flask import Flask , render_template , request


app = Flask(__name__)



@app.route('/')
def home():
    
    
    return render_template("index.html")


@app.route('/seed')
def seed():
    
    
    return render_template("seed.html")



if __name__ == '__main__':
    
    app.run(port=1940,debug=True)
