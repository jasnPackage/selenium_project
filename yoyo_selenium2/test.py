import hashlib
import json

md = hashlib.md5()#构造一个md5
md.update('jmy_123_AS*232'.encode())
# print(md.hexdigest())#加密后的字符串
#加密库
#   撞库
# 加盐
def md5_passwd(str,salt='123456'):
    #satl是盐值，默认是123456
    str=str+salt
    import hashlib
    md = hashlib.md5()  # 构造一个md5对象
    md.update(str.encode(encoding='utf-8'))
    res = md.hexdigest()
    return res



a = {"billNo":"889002169260","packageWeight":7600,"volumeList":[5011.0,2087.0,4100.0]}
a_n = json.dumps(a,separators=(',',':'))
salt = '1563268322000' + '123456'


import base64
def base64_jm():
    a = md5_passwd(a_n,salt)
    jm = base64.b64encode(a.encode('utf-8'))
    b = str(jm)
    print(b[2:-1])
    return b[2:-1]


c =  base64_jm()




import requests

kaolaWaybillUpdate_url = "http://edi-daily.xpm.cainiao.com/ext/gateway/kaolaWaybillUpdate/kaolaWaybillUpdate/api"

headers = {'Content-Type': 'application/json'}

data = {"logisCompanyCode":"422000","data":a_n,
        "sign":c,"type":"pushWeightInfo","timestamp":"1563268322000"}
print(data)

response = requests.post(url=kaolaWaybillUpdate_url,headers=headers,data=json.dumps(data))
print(response.text)