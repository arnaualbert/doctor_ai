import model.petition as petition
import model.login as logins
import random
import model.upload as uploa
new_petition: petition.Petition = petition.Petition("arnau","pep","pep","gordo","pep@gmail.com","admin") 
print(new_petition)
print(logins.petition_user(new_petition))



print(uploa.select_from_where_table("users","role_id",2))