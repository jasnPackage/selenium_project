import rsa
key = rsa.newkeys(3000)#生成随机秘钥
privateKey = key[1]#私钥
publicKey = key[0]#公钥
print(publicKey)



message ='{"order_id":"20181121000211022141241","version":"1.0","billno":"12365841"}'
print('Before encrypted:',message)
message = message.encode('utf-8')
cryptedMessage = rsa.encrypt(message, publicKey)
print('After encrypted:\n',cryptedMessage)
