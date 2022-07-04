from AQI_WebApp_Flask import app, forms
from flask import request, render_template
import os

photo = os.path.join('static')
app.config['folder'] = photo

@app.route('/', methods=['GET','POST'])
def search():
    searchForm = forms.AQIParameters(request.form)
    if request.method=="POST":
        '''
        If the user makes a post request, please save the selected value by the user into a variable
        Also, call the function aqi_parameter (from forms.py) with all the results
        Then, render template parameter_result.html only with the parameter requested by the user
        Which means that you should assign the correct value for the variable parameter_requested below
        '''
        data_entered = request.form["aqiparameter"]
        entire_dict= forms.aqi_parameter()
        parameter_requested = entire_dict[data_entered]

        file = os.path.join(app.config['folder'], "results.jpg")

        return render_template('parameter_result.html', result=parameter_requested, filename=file,everything=entire_dict,
                               param=data_entered)
    return render_template('parameter_search.html', form=searchForm)