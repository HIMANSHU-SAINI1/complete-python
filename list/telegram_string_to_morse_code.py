morse= [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",  # A–I
    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",  # J–R
    "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."          # S–Z
]
text='himanshu'
morse_str=''

for x in text:
    morse_str +=morse[ord(x)-97] + " "
print(morse_str)
