from flask import Flask, render_template, request
from tensorflow import keras
import numpy as np
app = Flask(__name__)

model = keras.models.load_model('dia_model.h5')



@app.route('/')
def home1():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def home():
  data1=request.form['a']
  data2=request.form['b']
  data3=request.form['c']
  data4=request.form['d']
  data5=request.form['e']
  data6=request.form['f']
  data7=request.form['g']
  data8=request.form['h']
  

  
  int_features = [[float (x) for x in request.form.values()]]
  final_features = [np.array(int_features)]
  prediction = model.predict(int_features)
  
  output = round(prediction[0][0])

  return render_template('after.html',data=output)



if __name__ == "__main__":
  app.run(debug=True)