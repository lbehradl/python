import re
def email_validation(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.[\w\.-]+$'
    return re.match(pattern, email)

res = email_validation(input())
if res:
    print('OK')
else:
    print('WRONG')

