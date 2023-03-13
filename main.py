import random
pas = ''
for x in range(11):
    pas = pas + random.choice(list('abcdefghigklmnopqrstuvyxwz1234567890'))
print('Your password is: ', pas)