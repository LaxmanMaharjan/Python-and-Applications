from encode import generate_jwt, SECRET_KEY

import jwt

def decode_jwt():
    token = generate_jwt()
    

    try:
        data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=['HS256']) 
        print(data)

    except jwt.ExpiredSignatureError:
        print({'message':'Token Expired'})

