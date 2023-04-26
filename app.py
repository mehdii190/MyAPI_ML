from flask import Flask , render_template , request
import joblib
from flower_form import FlowerForm




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



@app.route('/')
def home():
    
    
    return render_template("index.html")


@app.route('/seed')
def seed():
    
    
    return render_template("seed.html")



if __name__ == '__main__':
    
    app.run(port=1960,debug=True)
