
### Program made to check if a string is a legit KS license ####
### written by Eric M. Carter 11/15/15 ######
### Don't copy my code. >:( ####

import re

pattern = raw_input("Check if your string matches a Kansas license!" )

license = re.compile('^[A-Z]\d{8}$', re.UNICODE)
two_license = re.compile('^\d{9}$', re.UNICODE)
three_license = re.compile('^[A-Z]\d{1}[A-Z]\d{1}[A-Z]$', re.UNICODE)
match = license.search(pattern)
two_match = two_license.search(pattern)
three_match = three_license.search(pattern)

if match or two_match or three_match:
  print 'That is a match!'
else:
  print 'Not a match.'
