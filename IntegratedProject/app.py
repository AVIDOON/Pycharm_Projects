#import libraries
import numpy as np
import csv
from flask import Flask, request, jsonify, render_template
import pickle

#Initialize the flask App
app = Flask(__name__) 
model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict()

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Interest rate of this company is {}'.format(output))
# @app.route('/predict', methods=['GET', 'POST'])
# def upload_csv():
#     if request.method == 'POST':
#         csv_file = request.files['file']
#         print('hello world')
#     else:
#         return render_template('index.html')
        # print(csv_file)
        # csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        # csv_reader = csv.reader(csv_file, delimiter=',')
        # for row in csv_reader:
        #     user = User(username=row[0], email=row[1])
        #     db.session.add(user)
        #     db.session.commit()
        # return redirect(url_for('upload_csv'))
    # return """


if __name__ == "__main__":
    app.run(debug=True)