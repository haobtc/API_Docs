import requests
import json
import hashlib

def buildSign(params, secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) +'&'
    data = sign+'secret_key='+secretKey
    return  hashlib.md5(data.encode("utf8")).hexdigest().upper()

payload = {"api_key":"a06f5c1a-4ee8-45cd-ac3d-06dfdb27ec12", "amount":0.1, "price":3000, "type":"buy"}
sign = buildSign(payload, "c04cfbce-6f1b-40d4-a12e-b91b8be83063")
payload['sign'] = sign
r = requests.post("http://www.haobtc.com/api/exchange/v1/trade", data=payload)
print r.text

payload = {"api_key":"a06f5c1a-4ee8-45cd-ac3d-06dfdb27ec12", "order_id":57182}
sign = buildSign(payload, "c04cfbce-6f1b-40d4-a12e-b91b8be83063")
payload['sign'] = sign
r = requests.post("http://www.haobtc.com/api/exchange/v1/order_info", data=payload)
print r.text

payload = {"api_key":"a06f5c1a-4ee8-45cd-ac3d-06dfdb27ec12"}
sign = buildSign(payload, "c04cfbce-6f1b-40d4-a12e-b91b8be83063")
payload['sign'] = sign
r = requests.post("http://www.haobtc.com/api/exchange/v1/account_info", data=payload)
print r.text
