from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast
from dateutil.tz import *
from datetime import datetime
import pytz

# Check this command after running this file by using "python index.py" command
# Uses Python 3
# curl http://127.0.0.1:5000/date

app = Flask(__name__)
api = Api(app)

class Users(Resource):
	# users class for the URL
	def get(self):
		# This contains the local timezone 
		local = tzlocal()
		now = datetime.now()
		now = now.replace(tzinfo = local)

		# prints a timezone aware datetime
		# print now
		print(now.strftime("%a %b %d %H:%M:%S %Z %Y"))
		# returing data according to local format
		return {'date': now.strftime("%a %b %d %H:%M:%S %Z %Y")}
    
# Assigning URL for already defined claa
api.add_resource(Users, '/date')


if __name__ == '__main__':
    app.run()  # run our Flask app