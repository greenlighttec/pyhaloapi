from connecthaloapi import haloget

def getclients(id=None,showallobjects=None,search=None):
    parametersDict = {}
    resource = '/api/client'
    if id:
        resource = f'{resource}/{id}'
        showallobjects = True       
    if showallobjects: parametersDict['showallobjects'] = showallobjects
    if search: parametersDict['search'] = search
    # return results
    return haloget(resource,parametersDict)

def getusers(id=None,showallobjects=None,search=None):
    parametersDict = {}
    resource = '/api/users'
    if id:
        resource = f'{resource}/{id}'
        showallobjects = True       
    if showallobjects: parametersDict['showallobjects'] = showallobjects
    if search: parametersDict['search'] = search
    # return results
    return haloget(resource,parametersDict)
    
def gettickets(id=None,showallobjects=None,search=None):
    parametersDict = {}
    resource = '/api/tickets'
    if id:
        resource = f'{resource}/{id}'
        showallobjects = True       
    if showallobjects: parametersDict['showallobjects'] = showallobjects
    if search: parametersDict['search'] = search
    # return results
    return haloget(resource,parametersDict)

def getagents(id=None, me=False, **kwargs):
    parametersDict = {k: v for k, v in kwargs.items() if v is not None}
    resource = '/api/agent'
    if id:
        resource = f'{resource}/{id}'
    elif me:
        resource = f'{resource}/me'
    return haloget(resource, parametersDict)

def getassets(id=None, **kwargs):
    parametersDict = {k: v for k, v in kwargs.items() if v is not None}
    resource = '/api/asset'
    if id:
        resource = f'{resource}/{id}'
    return haloget(resource, parametersDict)
    
