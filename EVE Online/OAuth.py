# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:43:04 2021

@author: TN90072


https://developers.eveonline.com/blog/article/sso-to-authenticated-calls
"""
import requests
import json
import base64
import webbrowser
import swagger_client
from swagger_client.rest import ApiException
from swagger_client import Configuration


def char_info(character_id):
    ''' Get character's public information
    id = 94881232
    GET /characters/{character_id}/
    '''

    url = 'https://esi.evetech.net/latest/characters/{}/'.format(character_id)
    response = requests.get(url)
    # print(response.headers)
    char_info = json.loads(response.content)
    print(char_info["name"])


char_info(94881232)


def char_standings(character_id):
    ''' Get character's public information
    id = 94881232
    GET /characters/{character_id}/standings/
    '''
    
    ClientID = 'cd18a206505246f2835814af21b04f4f'
    Secret_Key = '9xoQwmEjQXEmJTyU1mmJmJYZKsHwg3WsDZQONCtT'
    Callback_URL = 'http://localhost/oauth-callback'
    scopes = "esi-characters.read_standings.v1"
    
    # URL has the following structure:
    # https://{login server base url}/oauth/authorize?response_type={response type}&redirect_uri={redirect uri}&client_id={client id}&scope={scopes}&state={state}
    
    # Our final URL looks like this:
    # https://login.eveonline.com/oauth/authorize?response_type=code&redirect_uri=http://localhost/oauth-callback&client_id={client id}&scope=esi-characters.read_standings.v1
    
    url = 'https://login.eveonline.com/oauth/authorize?response_type=code&redirect_uri={}&client_id={}&scope={}'.format(Callback_URL, ClientID, scopes)
    webbrowser.open_new_tab(url)
    
    authorization_code = input("Enter ?code= ")
    
    
    # To exchange the authorization code for an access token, we need to make a post request with curl.

    # The URL of the POST request has the following structure: https://{login server base url}/oauth/token
    
    exchange_url = "https://login.eveonline.com/oauth/token"
    '''
    We must send an Authorization header and a Content-Type header.
    The Content-Type can be application/json or application/x-www-form-urlencoded. We're going to use JSON.
    The Authorization header must be the word "Basic" followed by the base-64 encoded string of {client id}:{client_secret}. 
    If the client id was "client_id" and the secret was "clientsecret1", the final Authorization header value would be
    "Basic Y2xpZW50X2lkOmNsaWVudHNlY3JldDE=".
    '''
    # https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
    message = "{}:{}".format(ClientID, Secret_Key)
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    
    headers = {"Authorization":"Basic {}".format(base64_message)}
    body = {
      "grant_type": "authorization_code",
      "code": authorization_code
    } # aka payload
    
    # make curl request
    response = requests.post(exchange_url, params = body, headers = headers)
    result = json.loads(response.content)
    print(result)
    # access tokens are only valid for 20 minutes
    access_token = result["access_token"]
    
    # To get the character ID of a token
    url = "https://login.eveonline.com/oauth/verify"
    headers = {"Authorization":"Bearer {}".format(access_token)}
    response = requests.get(url, headers = headers)
    result = json.loads(response.content)
    print(result)
    
    CharacterID = result["CharacterID"]
    
    # Make an authenticated call.
    api = swagger_client.CharacterApi()
    api.api_client.set_default_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0') # Set a relevant user agent so we know which software is actually using ESI
    api.api_client.host = "https://esi.tech.ccp.is"
    Configuration().access_token = "{}".format(access_token) # fill in your access token here
    try:
        response = api.get_characters_character_id_standings({CharacterID}) # fill in the character id here
        print(response)
    except ApiException as e:
        print("Exception when calling CharacterApi->get_characters_character_id_standings: %s\n" % e)

    

