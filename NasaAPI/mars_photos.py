import requests, main_functions

# NASA's API url
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key="

# Read your NASA API key

#Build the final API url

#Make the API request

#Serialize the result to a JSON document

#Deserialize the recently create JSON document

#What is the type of the object deserialized?

#What are its keys?

#Access some of their values and their types passing their keys

#Create a set containing the names of all cameras

#Print the image source of the photos taken by the Navigation Camera

#Create a function that takes in a dictionary and a camera name
# and prints the image sources of all photos taken by the camera
# passed as argument and test this function.
def get_img_src(dataset,camera_name):
    #TODO: implement the get_img_src function

get_img_src(mars_pics,'Navigation Camera')