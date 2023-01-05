# 1. Ask for first name -- this will be used for personalization within the welcome email
# 2. Ask for email address
# 3. Validate email is correct with @ and .
# 4. If True, go to MailChimp account and trigger a Welcome email (API call)
# api_key: "9aa12571048fe85bd0636b43eff87edf-us18"
# "server": "us18"

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
  import mailchimp_marketing as MailchimpMarketing
  from mailchimp_marketing.api_client import ApiClientError

  mailchimp = MailchimpMarketing.Client()
  mailchimp.set_config({
    "api_key": "9aa12571048fe85bd0636b43eff87edf-us18",
    "server": "us18"
  })

  list_id = "4045e8295dAn"

  member_info = {
      "email_address": {email},
      "status": "subscribed",
      "merge_fields": {
        "FNAME": {firstname}
      }
    }

  try:
    response = mailchimp.lists.add_list_member(list_id, member_info)
    print("response: {}".format(response))
  except ApiClientError as error:
    print("An exception occurred: {}".format(error.text))
else:
  print('Looks like you haven\'t submitted an email address')