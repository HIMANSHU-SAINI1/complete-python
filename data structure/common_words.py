from collections import Counter
import re

text='''python s an easy programmers language.
pytho syntax is like the english language.
python language is easy to learn and adapt to compared with java and c
in python language,the same task can be performed using fewer lines of code
its easy learning and easy to code.'''



words=re.findall('\w+',text)
count=Counter(words)
print(count.most_common(3))