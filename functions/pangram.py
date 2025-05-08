def pangram(phrase):
    letter={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    phrase=set(phrase)
    if phrase >= letter:
        return True
    else:
        return False
    #or in place of if else we can also use
    #return phrase>=letter
    
print(pangram('abcdefghijklmnopqrstuvwxyz'))
print(pangram('the quick brown fox jumps over the lazy dog'))