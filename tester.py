############################# IMPORTS #############################
import model.login as test
import model.user as user
print()
print("############################# TEST LOGIN #############################")

print('----------------------------------------------------------------------')
print('Login fail')
print(test.login("arnau","1234"))
print('----------------------------------------------------------------------')
print()
print('----------------------------------------------------------------------')
print('Login success')
print(test.login('user0','123456'))
print('----------------------------------------------------------------------')
res = test.login('user0','123456')
print(res.username)
print(res.name)
print(res.surname)
print(res.email)
print(res.password)
