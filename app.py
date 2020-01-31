from flask import Flask,request,jsonify,session
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from model import generate
import uuid
import os

# instantiating the Flask class into app
app = Flask(__name__)

# instantiating the Api Class
api = Api(app)

# configurations 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or"sqlite:///generate.sqlite3"
app.config['SECRET_KEY'] = "abcd1234"


# instantiating the SQLAlchemy Class in db 
db=SQLAlchemy(app)

# this API is suppose to generate a random 
class generate_pin(Resource):

    def post(self):

        # the uuid funtion generates random 15 digits numbers
        a=str(uuid.uuid4().int)
        a.split()
        # specifying the length of numbers from uuid generated
        pin = a[:15]
        # creating a variable data and saving the value of the randomly generated pin
        data = generate(pin)

        # adding the pin to the database
        db.session.add(data)

        # commiting the new added item
        db.session.commit()

        # querying a column by the pin and saving it to the variable result
        result = generate.query.filter_by(pin = pin).first()
        
        # fetching the id of the particular pin and saving in s_N
        s_n = result.id
        return {'pin': pin, "SN":s_n }
        
api.add_resource(generate_pin, '/api/generator') 


class validate_pin(Resource):
    def post(self):
        # instantiating the request.get_json method to enable user to enter needed information
        request_data = request.get_json()

        # requesting a pin from user for validation
        pin = request_data['pin']
        sn = request_data['sn']

        # searching for that paticular pin in the database
        result1 = generate.query.filter_by(pin = pin).first()
        result2 = generate.query.filter_by(id = sn).first()
        
        # if pin is found it returns 1 for success
        if result1 == result2:
            return{"response":1}

        # else if pin is not found it returns o to represent failure
        else:
            return{"response": 0}    

api.add_resource(validate_pin, '/api/validator')         
    




if  __name__ == "__main__":
    
    app.run(debug=True)


