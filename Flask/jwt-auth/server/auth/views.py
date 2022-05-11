from flask import Blueprint, request, make_response, jsonify, send_from_directory
from flask.views import MethodView

from server import bcrypt, db, app
from server.models import User

auth_blueprint = Blueprint('auth',__name__)

class RegisterAPI(MethodView):
    """User Registration"""

    def get(self):
        return "Registration Page"

    def post(self):
        post_data = request.get_json()
        # if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()

        if not user:
            try:
                user = User(email = post_data.get('email'),name = post_data.get('name'),number = post_data.get('number'),password=post_data.get('password'),location=post_data.get('location'))

                db.session.add(user)
                db.session.commit()

                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401

        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202
            
class LoginAPI(MethodView):
    """
    User Login Resource
    """
    def post(self):
        # get the post data
        post_data = request.get_json()
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            if user and bcrypt.check_password_hash(
                user.password, post_data.get('password')
            ):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token
                    }
                    return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500

class UserAPI(MethodView):
    """
    User Resource
    """
    def get(self):
        # get the auth token
        auth_header = request.headers.get('Authorization')
        print(auth_header)
        print("type of auth header",type(auth_header))
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            print(resp)
            print(type(resp))
            if not isinstance(resp, str):
                print('from instance')
                print(resp)
                user = User.query.filter_by(id=resp).first()
                responseObject = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'location': user.location
                    }
                }
                return make_response(jsonify(responseObject)), 200
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 401

class JWKSView(MethodView):
    def get(self,filename):
        try:
            return send_from_directory(directory=app.config['JWKS'], path=filename)
        except FileNotFoundError:
            return make_response(jsonify({'message':"file not found"})), 404
    

# define the API resources
registration_view = RegisterAPI.as_view('register_api')
login_view = LoginAPI.as_view('login_api')
user_view = UserAPI.as_view('user_api')
jwks_view = JWKSView.as_view('jwks')

# add Rules for API Endpoints
auth_blueprint.add_url_rule(
        "/auth/register",
        view_func=registration_view,
        methods = ['POST',"GET"]
        )


auth_blueprint.add_url_rule(
        "/auth/login",
        view_func=login_view,
        methods = ['POST']
        )

auth_blueprint.add_url_rule(
        "/auth/profile",
        view_func=user_view,
        methods = ['GET']
        )

auth_blueprint.add_url_rule(
        "/public/.well-known/<filename>",
        view_func=jwks_view,
        methods = ['GET']
        )
