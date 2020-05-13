import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
from jsonRW import Json_manipulation
from decode import Caesar

r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=cc71e2cb7b30276bbcddd81a296c49e6dd492390')

d = Caesar()
text, json_new = d.cesar_alg_decrypt(r.json())
# print(text)
# print(json_new)

json_m = Json_manipulation()
json_m.write_json(json_new)

print(json_m.read_json())


answer = {'answer': open('answer.json', 'rb')}


r = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=cc71e2cb7b30276bbcddd81a296c49e6dd492390',
files=answer)

print(r.content)
