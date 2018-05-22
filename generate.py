from random import sample

LETTERS = 'rtyufghjvbnm'
MIN_NUM = -7

def main():
    words = []
    with open('words.txt') as f:
        for line in f:
            line = line.replace('\n', '')
            if containsLetters(line):
                words.append(line.lower())
    for x in sample(words, 20):
        print(x, end=' ')

def containsLetters(word):
    myletters = LETTERS
    counter = 0
    for x in word:
        if x in myletters:
            if MIN_NUM > 0:
                myletters = myletters.replace(x, '')
            counter += 1
    return counter > abs(MIN_NUM)


if __name__ == '__main__':
    main()
