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
