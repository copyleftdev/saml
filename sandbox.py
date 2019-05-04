import requests

with open("SAML_RESPONSE") as smlin:
    saml_response = smlin.read()
    print(saml_response)




callback_pl = {'SAMLResponse': saml_response, "RelayState": "http://localhost:3000/dashboard"}
header = {"Accept":"application/json"}
req = requests.head('http://192.168.247.111:8000/api/saml/callback', data=callback_pl, headers=header, verify=False)
res = req.text
print(res)
