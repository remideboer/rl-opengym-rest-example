from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse


app = Flask(__name__)
api = Api(app)


class DecideReminder(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        # look for json in body
        parser.add_argument('data', type =list, location='json')
        args = parser.parse_args()
        print(args)

        return 204

    def post(self):
        parser = reqparse.RequestParser()
        # look for json in body
        parser.add_argument('Authorization', location='headers', required=True)
        parser.add_argument('data', type =list, location='json', required=True)

        args = parser.parse_args()
        print(args)
        authHeader = args.get('Authorization')

        # split header on
        print(authHeader.split(" "))
        if not authHeader.split(" ")[0] == "Bearer":
            return {"message": "bad Authorization scheme"}, 400  # message in upper layer
        else:
             # check token
            if authHeader.split(" ")[1] == "123":
                return {"needReminder": True}, 200  # message in upper layer
            else:
                return {"message": "Unauthorized"}, 401  # message in upper layer



class Planner(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        # look for json in body
        parser.add_argument('data', type =list, location='json')
        args = parser.parse_args()
        print(args)

        return 204

    def post(self):
        parser = reqparse.RequestParser()
        # look for json in body
        parser.add_argument('Authorization', location='headers', required=True)
        parser.add_argument('data', type =list, location='json', required=True)

        args = parser.parse_args()
        print(args)
        authHeader = args.get('Authorization')

        # split header on
        print(authHeader.split(" "))
        if not authHeader.split(" ")[0] == "Bearer":
            return {"message": "bad Authorization scheme"}, 400  # message in upper layer
        else:
             # check token
            if authHeader.split(" ")[1] == "123":
                return {"needReminder": True}, 200  # message in upper layer
            else:
                return {"message": "Unauthorized"}, 401  # message in upper layer


api.add_resource(DecideReminder, '/need_reminder')
api.add_resource(Planner, '/planner')


if __name__ == '__main__':
    app.run(debug=True)