from flask import Flask,render_template
import random
import numpy as np
from io import StringIO
from io import BytesIO
import random
import pandas as pd 
import seaborn as sns 
import json

import matplotlib.pyplot as plt

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html') 


@app.route('/data', methods=['GET','POST'])
def employee():
    employee = []
    for i in range(1,10):
        employee.append(random.randint(0,10))
    data = {
        "emplyee": employee
    }
    return data


@app.route('/plot')
def build_plot():

  # Generate the plot
  x = np.linspace(0, 10)
  line, = plt.plot(x, np.sin(x))

  f = BytesIO()
  plt.savefig(f, format='png')

  # Serve up the data
  header = {'Content-type': 'image/png'}
  f.seek(0)
  data = f.read()

  return data, 200, header


@app.route('/test')
def initialize_df():
    df_employees_data = pd.DataFrame(columns=['time_step','value','employee','function'])
    df_employees_data = df_employees_data.append(
    {'time_step': 0,
     'employee': 0,
     'value': random.uniform(0,9),
     'function':'f1'}, ignore_index=True)

    df_employees_data = df_employees_data = df_employees_data.append(
    {'time_step': 0,
     'employee': 1,
     'value': random.uniform(0,9),
     'function':'f1'}, ignore_index=True)
    functions ={    
    'f1': {'a': 1, 'b1':0, 'b2':1},
    }
    default_fn = 'f1'
    data =df_employees_data.to_json()
    print(data)
    return data



# df_employees_data = initialize_df()

if __name__ == "__main__":
    app.run(debug=True)