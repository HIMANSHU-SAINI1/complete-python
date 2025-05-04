food=['pizza','nuggets','hotdog','pasta','burger']
letter=input("enter a letter")

for x in food:
    if x.startswith(letter):
        print(x)