"""HS256 (HMAC with SHA-256) is a symmetric algorithm, with only one (secret) key that is shared between the two parties. Since the same key is used both to generate the signature and to validate it, care must be taken to ensure that the key is not compromised.
"""
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'secret'
def generate_jwt():
    now = datetime.utcnow()
    payload ={
            'name':'laxman',
            'age': 23,
            'iat': datetime.utcnow(),
            'exp': (now + timedelta(hours=10)).timestamp()
            }
    return jwt.encode(payload=payload,key=SECRET_KEY, algorithm="HS256")

