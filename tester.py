############################# IMPORTS #############################
import model.login as test
import model.user as user
print()
print("############################# TEST LOGIN #############################")

print('----------------------------------------------------------------------')
print('Login fail')
print(test.login("asdasdsad","123213123123123"))
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
test.register('assssd','assssd','assssd','assssd','assssd',1)