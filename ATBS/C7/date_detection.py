import re, sys
# DD/MM/YYYY
# 1-31/01-12/1000-2999
# day and month will have leading zero if single digit

# April, June, September, and November have 30 days

#February has 28 days
#rest of the months have 31 days

date_regex = re.compile(r'''
([0-3][1-9])      #day
(\/)              #separator
([0-1][0-9])      #month
(\/)              #separator  
([1-2][0-9]{3})   #year
''', re.VERBOSE)
date_mo = date_regex.search('29/02/2221')

day, month, year = date_mo.group(1), date_mo.group(3), date_mo.group(5)

# days mapped to months in number form
valid_dates = {
  30: ['Apr', 'Jun', 'Sep', 'Nov'],
  28: ['Feb'],
  31: ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
  }

months = {
  '01': 'Jan', '02': 'Feb', '03': 'Mar',
  '04': 'Apr', '05': 'May', '06': 'Jun', 
  '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct',
  '11': 'Nov', '12': 'Dec'}


def get_key(month):
  for k, v in valid_dates.items():
    if month in v:
      return k

def is_date_valid():
  if int(day) <= get_key(months[month]):
    print('date is valid')
  else:
    print('date is invalid')


# check if leap year
if months[month] == 'Feb' and int(day) == 29:
    if int(year) % 4 == 0 and int(year) % 100 != 0:
      print('date is valid')
    else:
      is_date_valid()
else:
  is_date_valid()

  