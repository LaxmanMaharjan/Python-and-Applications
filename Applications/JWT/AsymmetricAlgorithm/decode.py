import jwt
from encode import generate_jwt
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def decode_and_validate_token(token):
    try:
        unverified_headers = jwt.get_unverified_header(token)
        with open("./keys/public_key.pem", 'r') as file:
            public_key_text = file.read()

        #public_key = load_pem_x509_certificate(public_key_text.encode()).public_key()
        public_key = public_key_text.encode()
        #public_key = serialization.load_pem_public_key(public_key_bytes,backend=default_backend())
    


    
        return jwt.decode(
            token,
            key=public_key,
            algorithms = unverified_headers["alg"]
            )
    except Exception as e:
        print("type of e",type(e))
        print(repr(e))
        print(str(e))



print(decode_and_validate_token(generate_jwt()))
