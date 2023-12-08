from flask import Flask, request, jsonify, render_template


app = Flask(__name__)



from funcion_calculadora_basica import calculadora_basica


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = calculadora_basica(a,b,operation)

    return render_template('index.html', prediction_text=str(result))


if __name__ == "__main__":
    app.run(debug=True)