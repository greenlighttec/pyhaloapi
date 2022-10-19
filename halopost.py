from connecthaloapi import halopost

## Update Options will start with "set"
def setclients(client):
    resource = '/api/client'
    postBody = client
    for listItem in postBody:
        if not listItem['id']:
            print('Client ID must be specified when updating a client')
            return False
    else:
        return halopost(resource,postBody)




