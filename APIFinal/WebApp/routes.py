from WebApp import app, forms
from flask import request, render_template
import os


@app.route('/', methods=['GET','POST'])
def search():
    searchForm = forms.WebsiteParameters(request.form)
    if request.method=="POST":
        '''
        If the user makes a post request, please save the selected value by the user into a variable
        Also, call the function aqi_parameter (from forms.py) with all the results
        Then, render template parameter_result.html only with the parameter requested by the user
        Which means that you should assign the correct value for the variable parameter_requested below
        '''
        name_entered = request.form["name"]
        crypto_entered = request.form["cryptoCoin"]
        websec_entered = request.form["websiteParameter"]
        entire_dict = forms.search_parameters(crypto_entered, websec_entered)

        return render_template('parameter_result.html', name=name_entered, website=websec_entered, crypt=crypto_entered,
                               everything=entire_dict)
    return render_template('parameter_search.html', form=searchForm)