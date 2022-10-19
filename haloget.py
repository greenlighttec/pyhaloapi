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
    
