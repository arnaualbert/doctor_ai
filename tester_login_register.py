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
print(test.login('arnau','1234'))
print('----------------------------------------------------------------------')
res = test.login('arnau','1234')
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
