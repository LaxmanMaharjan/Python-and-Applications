import requests
import jwt
import json
from encode import generate_jwt

url = "http://127.0.0.1:5000/public/.well-known/jwks.json"
public_keys = requests.get(url=url).json()

jwk = public_keys["keys"][0]

token = generate_jwt()
unverified_headers = jwt.get_unverified_header(token)

print(public_keys)
print(type(public_keys))
print(jwk)

public_key = jwt.algorithms.RSAAlgorithm.from_jwk(jwk)
#public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

print(public_key)


# Now use the key to verify and decode your token
payload = jwt.decode(token, key=public_key, algorithms=unverified_headers['alg'])

print("Payload is ")
print(payload)
