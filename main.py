import random
pas = ''
for x in range(11):
    pas = pas + random.choice(list('abcdefghigklmnopqrstuvyxwz'))
print('Your password is: ', pas)