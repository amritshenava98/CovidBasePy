from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import jsonify
from flask import make_response
#import firebase_admin
#from firebase_admin import credentials 
#from firebase_admin import db
from firebaseconfig import config
import json
import pyrebase


#cred = credentials.Certificate("path/to/serviceAccountKey.json")
#firebase_admin.initialize_app(cred)


#firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://databaseName.firebaseio.com'
#})

#ref = db.reference('restricted_access/secret_document')
#ref = db.reference('leads')
#print(ref.get())


firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    query_result = req.get('queryResult')
    resource = str(query_result.get('parameters').get('resource'))
    city = str(query_result.get('parameters').get('geo-city'))
    lead = db.child('leads').get()
    if(resource == lead.val().get('resource')) & (city == lead.val().get('city')):
      info = lead.val()['info']
      response = resource + " is available in " + city + " and here is the info we have " + info
      print(response)
    else:
      response = "We do not have a lead"
      print(response)
    return response

    #if action == 'get_resource':
     # res = get_resource(req)

    #print('Action: ' + action)
    #print('Response: ' + res)

    #return make_response(jsonify({'fulfillmentText': response}))

    return {
      'fulfillmentText': response
    }

#def get_resource(req):
    #query_result = req.get('queryResult')
    #resource = query_result.get('parameters').get('resource')
    #city = query_result.get('parameters').get('geo-city')
    #lead = db.child('leads').get()
    #if(resource == lead.val()['resource']) & (city == lead.val()['city']):
      #info = lead.val()['info']
      #response = resource + " is available in " + city + " and here is the info we have " + info
      #print(response)
    #else:
      #response = "We do not have a lead"
      #print(response)
    #return response
  
    
    

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)
