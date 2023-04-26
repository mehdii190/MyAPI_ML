from flask import Flask , request, jsonify, session, url_for, redirect, render_template
import joblib
from flower_form import FlowerForm
import os



classifier_loaded = joblib.load("C:/Users/persian computer/Desktop/file/MyAPI_ML/save models/01.knn_with_iris_dataset.pkl")
encoder_loaded = joblib.load("C:/Users/persian computer/Desktop/file/MyAPI_ML/save models/02.iris_label_encoder.pkl")


# prediction function
def make_prediction(model, encoder, sample_json):
    # parse input from request
    SepalLengthCm = sample_json['SepalLengthCm']
    SepalWidthCm = sample_json['SepalWidthCm']
    PetalLengthCm = sample_json['PetalLengthCm']
    PetalWidthCm = sample_json['PetalWidthCm']

    # Make an input vector
    flower = [[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]]

    # Predict
    prediction_raw = model.predict(flower)

    # Convert Species index to Species name
    prediction_real = encoder.inverse_transform(prediction_raw)

    return prediction_real[0]



app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def home():
    
    
    return render_template("index.html")


@app.route('/seed' , methods=['GET','POST'])
def seed():
    
    form = FlowerForm()

    if form.validate_on_submit():
        session['SepalLengthCm'] = form.SepalLengthCm.data
        session['SepalWidthCm'] = form.SepalWidthCm.data
        session['PetalLengthCm'] = form.PetalLengthCm.data
        session['PetalWidthCm'] = form.PetalWidthCm.data

        return redirect(url_for("predSeed"))
    return render_template("seed.html", form=form)

@app.route('/predSeed')
def predSeed():
    
    content = {'SepalLengthCm': float(session['SepalLengthCm']), 'SepalWidthCm': float(session['SepalWidthCm']),
               'PetalLengthCm': float(session['PetalLengthCm']), 'PetalWidthCm': float(session['PetalWidthCm'])}

    results = make_prediction(classifier_loaded, encoder_loaded, content)

    return render_template('predSeed.html', results=results)



if __name__ == '__main__':
    
    app.run(port=1960,debug=True)
