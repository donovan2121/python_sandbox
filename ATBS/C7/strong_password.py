import re 

#create 3 regex
#regex 1 - at least 8 chars
#regex 2 - containers both Uppercase and Lowercase
#regex 3 - at least 1 digit

regex1 = re.compile(r'\w{8,}')
regex2 = re.compile(r'[a-z]+')
regex3 = re.compile(r'[A-Z]+')
regex4 = re.compile(r'\d+')

def check_password(text):
  
  mo1 = regex1.search(text)
  mo2 = regex2.search(text)
  mo3 = regex3.search(text)
  mo4 = regex4.search(text)
  
  # checks regex 1 and 4

  # try/except to handle no attribute 'group' error
  try:
    if len(mo1.group()) >= 8 and len(mo4.group()) >=1:
      # checks regex 2 and 3
      if len(mo2.group()) >= 1 and len(mo3.group()) >= 1:
        return True
  except:
    return False


while True:
  print('Enter a strong password:', end=' ')
  password = input()

  if check_password(password):
    print('Strong Password')
    break
  else:
    print('Weak Password. Enter a stronger password')
    