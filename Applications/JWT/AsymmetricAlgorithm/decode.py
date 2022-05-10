import jwt
from encode import generate_jwt
from cryptography.x509 import load_pem_x509_certificate

def decode_and_validate_token(token):
    unverified_headers = jwt.get_unverified_header(token)
    with open("./Keys/public_key.pem", 'r') as file:
        public_key_text = file.read()
    public_key = load_pem_x509_certificate(public_key_text.encode()).public_key()

    return jwt.decode(
            token,
            key=public_key,
            algorithms = unverified_headers["alg"]
            )



#print(decode_and_validate_token(generate_jwt()))
