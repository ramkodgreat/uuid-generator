# Auto_Pin-genarating-API
once a request is sent to the API it automatically generates a pin and serial number for user. 
I created a model.py file which handles the creation of database using SQLAlchemy.
in my model.py i created a class called generate as the name of my database
i use sqlite as my database.
i create an app.py file to handle my APIs.
the endpoint for generating pin and serial number is api.add_resource(generate_pin, '/api/generator') 
the endpoint for validating pin and serial number is api.add_resource(validate_pin, '/api/validsn/sn')
the endpoint for validating pin and serial number is api.add_resource(validate_pin, '/api/validpin/pin')
the validation endpoint returns 1 if pin is valid and 0 if invalid
the link to the app is https://uuidcreater.herokuapp.com
