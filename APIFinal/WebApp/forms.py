from WebApp import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField

class WebsiteParameters(FlaskForm):
    name = StringField('name')
    cryptoCoin = StringField('cryptoCoin')
    websiteParameter = SelectField("Which website would you "
                                   " like to analyze and receive their"
                                   " grade on? ", choices=[
        ("www.google.com", "Google"),
        ("www.facebook.com", "FaceBook"),
        ("www.youtube.com", "YouTube"),
        ("www.bing.com", "Bing")
    ])

def search_parameters(cryptocoin,websitesec):
    url_crypto = "http://api.coinlayer.com/live?access_key="
    url_security = "https://http-observatory.security.mozilla.org/api/v1/analyze?host="

    crypto_key = main_functions.read_from_file("WebApp/JSON_Files/crypto_key.json")
    crypto_key = crypto_key["crypto_key"]

    url_crypto_key = url_crypto + crypto_key + "&symbols=" + str(cryptocoin)
    url_security_key = url_security + websitesec

    requests_json = requests.get(url_crypto_key).json()
    request_json_1 = requests.get(url_security_key).json()

    main_functions.save_to_file(requests_json, "WebApp/JSON_Files/cryptoData.json")
    main_functions.save_to_file(request_json_1, "WebApp/JSON_Files/websecData.json")

    crypto_index = main_functions.read_from_file("WebApp/JSON_Files/cryptoData.json")
    websec_index = main_functions.read_from_file("WebApp/JSON_Files/websecData.json")

    cryptoprice = crypto_index["rates"][str(cryptocoin)]
    websecgrade =  websec_index["grade"]

    parameters = {
        'cryptoprice': cryptoprice,
        'websecgrade': websecgrade
    }
    return parameters


