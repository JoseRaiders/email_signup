# 1. Ask for first name -- this will be used for personalization within the welcome email
# 2. Ask for email address
# 3. Validate email is correct with @ and .
# 4. If True, go to MailChimp account and trigger a Welcome email (API call)

import re

firstname = input('What is your name: ')
print(f'Hello, {firstname}!')
email = input('Please enter your email address: ')

def isvalidEmail(email):
    pattern = "^\S+@\S+\.\S+$"
    objs = re.search(pattern, email)
    try:
        if objs.string == email:
            return True
    except:
        return False

if email:
  email_address = isvalidEmail(f'{email}')
  print(email_address)
else:
  print('Looks like you haven\'t submitted an email address')
