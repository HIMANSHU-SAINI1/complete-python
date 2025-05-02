# import re

# re.match('abc','abcdef')
# re.fullmatch('python','python').group() #group will give the string


# re.search('very','python is very easy').span() #span will give the indices

# re.findall('can','can you can a can as a canner')


# import re
# re.fullmatch('(ab)+','ababababab')
# re.fullmatch('(ab)*','ababababab')
# re.fullmatch('(ab)?','ab')
# re.fullmatch('(ab){4}','abababab')
# re.fullmatch('(ab){4,5}','ababababab')


#a pattern to find or check first name or last name
import re
re.fullmatch('[A-Z][a-z]+ [A-Z][a-z]+','Himanshu Saini')

# a pattern for date
'\d{2}/\d{2}/\d{4}'

