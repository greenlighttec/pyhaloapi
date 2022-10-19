# Initial HaloAPI Function
from datetime import datetime,timedelta
import requests
import json

def lookupauthurl(url,additionalheaders=None):
    url = url + '/api/authinfo/'
    authInfo = requests.get(url,headers=additionalheaders)
    return authInfo

def connect(url,clientid,clientsecret,additionalheaders=None,scopes="all"):
    global HAPILoginInfo
    HAPILoginInfo = {}
    HAPILoginInfo['clientid'] = clientid
    HAPILoginInfo['clientsecret'] = clientsecret
    HAPILoginInfo['additionalheaders'] = additionalheaders
    HAPILoginInfo['scopes'] = scopes
    global HAPIConnectionInfo
    HAPIConnectionInfo = {}
    HAPIConnectionInfo['baseUrl'] = url
    if isinstance(scopes,list):
        scopes = ' '.join(scopes)
    if url and clientid and clientsecret:
        authInfo = lookupauthurl(url,additionalheaders)
        if authInfo.status_code == 200:
            requestHaloAuthBody = {}
            requestHaloAuthBody['client_secret'] = clientsecret
            requestHaloAuthBody['client_id'] = clientid
            requestHaloAuthBody['grant_type'] = 'client_credentials'
            requestHaloAuthBody['scope'] = scopes                     
            tokenRequest = requests.post(authInfo.json()['auth_url'] +'/token',data=requestHaloAuthBody)
            # Setup the Expiration time to check each time a command runs, if the expiration time has passed, refresh the token 
            HAPIConnectionInfo['tokenExpiryTime'] = datetime.now() + timedelta(seconds=tokenRequest.json()['expires_in'])
            HAPIConnectionInfo['token'] = tokenRequest.json()['access_token']
            HAPIConnectionInfo['refreshToken'] = tokenRequest.json()['refresh_token']

def refreshconnection():
    connect(HAPIConnectionInfo['baseUrl'],**HAPILoginInfo)

def halowebrequest(method,urlpath,postbody=None):
    if datetime.now() > HAPIConnectionInfo['tokenExpiryTime']:
        refreshconnection()
    apiHeaders = {}
    apiHeaders['Authorization'] = 'Bearer ' + HAPIConnectionInfo['token']
    apiHeaders['Content-Type'] = 'application/json'

    if method == 'GET':
        haloResponse = requests.get(HAPIConnectionInfo['baseUrl'] + urlpath,headers = apiHeaders)
    elif method == 'POST':
        print(f'Submitting Post request to {HAPIConnectionInfo["baseUrl"]}{urlpath} with body {postbody}')
        haloResponse = requests.post(url = HAPIConnectionInfo['baseUrl'] + urlpath,data = postbody,headers = apiHeaders)
        
    if haloResponse.status_code == 200 or haloResponse.status_code == 201:
        return haloResponse.json()
    else:
        print(f'An error occurred while making an http request. API Returned status code: {haloResponse.status_code}')
        print(haloResponse.text)

def haloget(resource, query=None):
    if isinstance(query,dict):
        query = '&'.join(f'{key}={value}' for key, value in query.items())
        ApiCall = resource + '?' + query
    else:
        ApiCall = resource
    return halowebrequest('GET',ApiCall)

def halopost(resource,data):
    if not isinstance(data,list):
        print('You must pass a proper DICT type of data wrapped within a LIST for the post')
        return False
    else:
        newArray = [listItem for listItem in data if isinstance(listItem,dict)]
        if len(newArray) != len(data):
            print('You must pass a proper DICT type of data wrapped within a LIST for the post payload')
            return False

        ApiCall = resource
        data = json.dumps(data)
        return halowebrequest('POST',ApiCall,data)
