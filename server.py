from flask import Flask, request
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_yaml
import json
import numpy as np
import itertools

app = Flask(__name__)

req = ""

#import tensorflow as tf
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

@app.route("/is_dab", methods=['POST','OPTIONS'])
def is_dab():
    data = request.form.get('data')
    merged = list(itertools.chain.from_iterable(data))
    merged = list(itertools.chain.from_iterable(merged))
    merged = [round(float(x),2) for x in merged]
    data2 = np.array(merged)
    df = pd.DataFrame(data2)
    ans = loaded_model.predict()
    return ans

if __name__ == '__main__':
    app.run(host='0.0.0.0')
