from connecthaloapi import halopost

## Update Options will start with "set"
def setclients(client):
    resource = '/api/client'
    postBody = client
    for listItem in postBody:
        if not listItem.get('id'):
            print('Client ID must be specified when updating a client')
            return False
    else:
        return halopost(resource,postBody)

def setusers(user):
    resource = '/api/users'
    postBody = user
    for listItem in postBody:
        if not listItem.get('id'):
            print('User ID must be specified when updating a user')
            return False
    else:
        return halopost(resource, postBody)

def settickets(ticket):
    resource = '/api/tickets'
    postBody = ticket
    for listItem in postBody:
        if not listItem.get('id'):
            print('Ticket ID must be specified when updating a ticket')
            return False
    else:
        return halopost(resource, postBody)




