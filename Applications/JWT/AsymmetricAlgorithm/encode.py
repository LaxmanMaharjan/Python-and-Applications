import jwt
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization

def generate_jwt():
    now = datetime.utcnow()
    payload ={
            'name':'laxman',
            'age': 23,
            'iat': datetime.utcnow(),
            'exp': (now + timedelta(hours=10)).timestamp()
            }
    with open('./Keys/private_key.pem','r') as file:
        private_key_text = file.read()


    private_key = serialization.load_pem_private_key(
        private_key_text.encode(), password=None
    )
    return jwt.encode(payload=payload, key=private_key, algorithm="RS256")
