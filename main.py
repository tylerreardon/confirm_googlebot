from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import confirm_googlebot


app = Flask(__name__)
api = Api(app)
CORS(app)

class googlebotChecker(Resource):
    def get(self, ip_list):
        ip_list = ip_list.replace('_', '.')
        return {'real_googlebots': confirm_googlebot.run([ip_list])}
        

api.add_resource(googlebotChecker, '/confirm_googlebot/<ip_list>')



@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()