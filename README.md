# pyhaloapi
Python Module for HaloPSA and sister software

This is my very first python project, and this is styled after @homotechsual's HaloAPI powershell module
www.github.com/homotechsual/haloapi

## Instructions
Clone/download and extract the files and save it into your python project folder.

- Add "import pyhaloapi.pyhaloapi" into your project to import the main file.
- All commands will be available under the "pyhaloapi" namespace.

### Connecting to HaloAPI
Run the "pyhaloapi.connect()" function filling in parameters such as url, clientid, clientsecret, additionalheaders and scope. 

additionalheaders parameter is used for a bypass header to override the API throttling or other security measures if you have this. It is an optional parameter.

scope is a mandatory parameter that will default to "all"

### Module Structure
This is a framework design, all web queries get built and passed up the framework to a handler. Tokens and core functions are performed in the connecthaloapi.py file.

Any GET web request will occur in the haloget.py
Any POST web requests will occur in the halopost.py

Parameters should specifically match the API parameters of Halo itself 

Token will refresh automatically after expiry time using the ClientID/ClientSecret as documented.

### Adding new endpoints

#### GET endpoints
 - Under the haloget.py add a new function for the new endpoint, include the parameters you want to allow including search strings or specific filtering parameters.

- set the "resource" variable to be the new endpoint you want to hit
- the parameters should be passed into a dict object (key/value pair) of HaloPSA API expected parameters and values. The python module will convert this automatically into a query string when buidling the web request.

- Note that when returning a list of objects the result will be an array under the "clients" property of a dict object, when returning a single object it'll be by itself.

#### POST endpoints
- Under the halopost.py add a new function for the endpoint, for a POST the a dict object wrapped into a list should be provided to the function, and the function will pass it onto the Halo POST handler module which will stringify it into JSON and make the web call.

- There are types of post requests, SET and NEW. When using SET the function should validate that an ID item exists so you don't accidentally create duplicates. When using NEW the function should validate no ID exists so you don't overwrite something.
