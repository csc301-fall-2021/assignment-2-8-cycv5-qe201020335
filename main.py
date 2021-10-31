from flask import Flask, request, Response
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# post_arg = reqparse.RequestParser()
# post_arg.add_argument("name", type=str, help="Name of the file")


@app.route('/time_series/<type>', methods=['POST', 'PUT'])
def upload_time_series():
    file = request.files['file']

    s = str(file.readline())
    return {"first line in the file": s}


@app.route('/daily_reports/', methods=['POST', 'PUT'])
def upload_daily_reports():
    file = request.files['file']
    s = str(file.readline())
    return {"first line in the file": s}


@app.route('/cases/<place>/<info>', methods=['GET'])
def get_info(place, info):
    return {"place": place, "info": info}


if __name__ == "__main__":
    app.run(debug=True)  # TODO: change to false for production
