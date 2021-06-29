import requests as r
import json


_TOKEN = "EAAHnSrlmBj4BAAlzMjKpdifhDpWx4Q6SFywVfFW1VRvBihSmy3PuXffByAZCQ7KthP9 \
    YnqPnS5pcOcw1XOjRWhCkfj22qK8np5RqFCqZCSpkKSomKYQot1pvHigfCwT5GT0HEWGPRIy3 \
        siIPZCA6Tx6C6u6HHgZCvuMgYyR2txKW0itCatw4"
        

_PARAMS = dict()
_PARAMS["base_url"] = "https://graph.facebook.com/"
_PARAMS["api_version"] = "v11.0/"

def get_user_page(token=_TOKEN,params=_PARAMS) :
    request = params["base_url"] + params["api_version"]
    request += "me/accounts?access_token="
    request += token
    response = r.get(request)
    return(json.loads(response.text))

_USER_PAGE = get_user_page()

def get_page_accessToken(token=_TOKEN,params=_PARAMS, user_page = _USER_PAGE) :
    request = _PARAMS["base_url"] 
    page_id = user_page['data'][1]['id']
    request += page_id + '?'
    request += 'fields=access_token&access_token=' + token
    response = r.get(request)
    return(json.loads(response.text))

_ACCESS_TOKEN = get_page_accessToken()['access_token']

def get_inbox_convIds(token=_TOKEN,params=_PARAMS,page_id=_USER_PAGE['data'][1]['id'], \
                         accessToken=_ACCESS_TOKEN) :
    request = params["base_url"] + params["api_version"]
    request += page_id + '/conversations?platform=instagram'
    request += '&access_token=' + accessToken
    response = r.get(request)
    return(json.loads(response.text))

_INBOX_CONV_IDS = get_inbox_convIds()


def get_messages_ids(token=_TOKEN,params=_PARAMS,page_id=_USER_PAGE['data'][1]['id'], \
                     accessToken=_ACCESS_TOKEN, inbox_conv_ids=_INBOX_CONV_IDS) :
    request = params["base_url"] + params["api_version"]
    thread_id = inbox_conv_ids['data'][0]['id']
    request += thread_id + '?fields=messages'
    request += '&access_token=' + accessToken
    response = r.get(request)
    return(json.loads(response.text))

_MESSAGES_IDS = get_messages_ids()

def get_message(token=_TOKEN,params=_PARAMS,page_id=_USER_PAGE['data'][1]['id'], \
                     accessToken=_ACCESS_TOKEN, messages_ids=_MESSAGES_IDS) :
    request = params["base_url"] + params["api_version"]
    message_id = messages_ids['messages']['data'][0]['id']
    request += message_id + '?fields=story'
    request += '&access_token=' + accessToken
    response = r.get(request)
    return(json.loads(response.text))

_MESSAGE = get_message()
print(_MESSAGE)

_IGSID = '6341037472603944'

def get_user_infos(params=_PARAMS,igsid=_IGSID,accessToken=_ACCESS_TOKEN) :
    request = params["base_url"] + params["api_version"]
    request += igsid
    request += '?fields=name,profile_pic&access_token=' + accessToken
    response = r.get(request)
    return(json.loads(response.text))

#USER_INFO = get_user_infos()
#print(USER_INFO)

