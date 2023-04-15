############################# IMPORTS #############################
import model.login as test
import model.user as user
import multiprocessing
import hashlib
print()
print("############################# TEST LOGIN #############################")

print('----------------------------------------------------------------------')
print('Login fail')
print(test.login("lolo","lolo"))
print('----------------------------------------------------------------------')
print()
print('----------------------------------------------------------------------')
print('Login success')
password = "1234"
enc_pass = hashlib.sha256(password.encode()).hexdigest()
print(test.login('arnau',enc_pass))
print('----------------------------------------------------------------------')
res = test.login('arnau',enc_pass)
print(res.username)
print(res.name)
print(res.surname)
print(res.email)
print(res.pass_hash)

print()
print("############################# TEST REGISTER #############################")
print('----------------------------------------------------------------------')
print('Register fail')
print(test.register('asdfxcvxzcv','nasdasasdfafddame','surname','email','pass',1))
print('----------------------------------------------------------------------')
print()
print('----------------------------------------------------------------------')
print('Register success')
print(test.register('asd','asd','asd','asd','asd',1))
print(test.login('ola','ola'))
