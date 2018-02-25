"""File containing function utilised by the app"""
import json

import requests as req

import config as conf

#Fonction de test à supprimer
def make_text(question):
    """Fonction pour test"""
    return 'Vous avez saisi : ' + question

def parser(question):
    """Function used to parse the question of the user
    Remove the word containing in the stopword base to keep
    only key words"""
    list_word = question.split()
    with open('pybot/stopwords.json', 'r') as file:
        stopwords = json.load(file)
        for word in list_word:
            if word in stopwords:
                list_word.remove(word)
    key_words = " "
    return key_words.join(list_word)

def request_api(url):
    """Request the selected url and return data from the api as json"""
    data = req.get(url)
    return data.json()

def get_data_from_google_maps(keywords):
    """Do request to the google maps API"""
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}".format(\
        keywords, conf.GOOGLE_MAPS_KEY)
    data = request_api(url)
    result_lat = data["results"][0]["geometry"]["location"]["lat"]
    result_long = data["results"][0]["geometry"]["location"]["lng"]
    return result_lat, result_long

def get_data_from_media_wiki(keywords):
    pass