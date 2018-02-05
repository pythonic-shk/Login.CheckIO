#the most frequent letter

def checkio(text):
    freq = 0
    alphalist = []
    letter = ''
    Ftext = text.lower()
    
    for c in Ftext:
        if c.isalpha():
            if Ftext.count(c) > freq:
                freq = Ftext.count(c)
                letter = c
                alphalist = list(c)
            elif Ftext.count(c) == freq:
                alphalist.append(c)
                letter = min(alphalist)
    return letter

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")