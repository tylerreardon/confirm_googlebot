from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import confirm_googlebot


app = Flask(__name__, static_folder='static', static_url_path='')
api = Api(app)
CORS(app)

class googlebotChecker(Resource):
    def get(self, ip_list):
        ip_list = ip_list.replace('_', '.')
        return {'real_googlebots': confirm_googlebot.run([ip_list])}
        

api.add_resource(googlebotChecker, '/confirm_googlebot/<ip_list>')



@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
