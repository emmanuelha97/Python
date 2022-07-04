import main_functions
import requests

# NASA's API url
url = "https://api.nasa.gov/planetary/apod?api_key="

# Read your NASA API key
nasa_key = main_functions.read_from_file("nasaKey.json")
nasa_key_str = nasa_key["nasa_key"]
# Build the final API url
final_url = url + nasa_key_str
# Make the API request
response = requests.get(final_url).json()
# Serialize the result to a JSON document
main_functions.save_to_file(response, "apod.json")
# Deserialize the recently create JSON document
# apod = main_functions.read_from_file("apod.json")
# What is the type of the object deserialized?

# What are its keys?

# Access some of their values passing their keys
