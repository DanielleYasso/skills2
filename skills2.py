string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def clean_word(word):
    word = word.strip(" .!?,;:-_\"'*()[]")
    if "--" in word:
        more_words = word.split("--")
        for new_word in more_words:
            return new_word
    else:
        return word

def count_unique(string1):
    d = {}
    letter_count = {}
    f = open(string1)
    for line in f:
        word_list = line.strip().split()
        for word in word_list:
            word = clean_word(word)
            if word == "":
                continue
            d[word] = d.get(word, 0) + 1
            for letter in word:
                letter_count[letter] = letter_count.get(letter, 0) + 1 
        
    for word in sorted(d.keys()):
        print "\"%s\" appears %d times" % (word, d[word])
    for letter in sorted(letter_count.keys()):
        print "\"%s\" character appears %d times" % (letter, letter_count[letter])

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    common_list = []

    for item in list1:
        for item2 in list2:
            if item == item2:
                common_list.append(item)
        # if list2.__contains__(item):
        #     if common_list.__contains__(item):
        #         continue
        #     else:
        #         common_list.append(item)

    return common_list


"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    d = {}
    common_list = []
    for item in list1:
        d[item] = 1
    for item in list2:
        if d.get(item, 0) == 1:
            common_list.append(item)
    return common_list

"""
Given a list of numbers, return list of number pairs that sum to zero
Try as a dictionary
"""
def sum_zero(list1):
    zero_sums = []
    d = {}
    for num in list1:
        d[num] = True # add number as key in dictionary
        if d.get(-num, False):
            zero_sums.append((num, -num))
    # for key in d.keys():
        # if d.get(-key, False): # for each key, is there a matching negative key
            # zero_sums.append((key, -key))
    return zero_sums


"""
Given a list of words, return a list of words with duplicates removed
Try as a dictionary - not set 
"""
def find_duplicates(words):
    d = {}
    for word in words:
        d[word] = True
    words_list = d.keys()
    return words_list

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(filename):
    d = {}
    f = open(filename)
    for line in f:
        line = line.strip()
        words_list = line.split()
        for word in words_list:
            word = clean_word(word).upper()
            if word == "":
                continue
            length = len(word)
            d.setdefault(length, []).append(word)

    for length in sorted(d.keys()):
        print "Words with a length of %d:" % length
        word_list_for_length = find_duplicates(d[length])
        for word in word_list_for_length:
            print word


"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
def pirate():
    user_input = raw_input("Type a sentence! ")
    print "Converting to pirate speak..."

    pirate_speak = {"sir": "matey",
                    "hotel": "fleabag inn",
                    "student": "swabbie",
                    "boy": "matey",
                    "madam": "proud beauty",
                    "professor": "foul blaggart",
                    "restaurant": "galley",
                    "your": "yer",
                    "excuse": "arr",
                    "students": "swabbies",
                    "are": "be",
                    "lawyer": "foul blaggart",
                    "the": "th'",
                    "restroom": "head",
                    "bathroom": "head",
                    "my": "me",
                    "hello": "avast",
                    "is": "be",
                    "man": "matey",
                    "friend": "matey",
                    "hi": "avast"}

    user_words = user_input.strip().split()

    # convert to pirate!
    for i, word in enumerate(user_words):
        word = word.lower()
        if pirate_speak.get(word, False):
            user_words[i] = pirate_speak[word]

    pirate_message = " ".join(user_words)
    print pirate_message


def main():
    print "Count unique:"
    count_unique("twain.txt")

    print "Common items:"
    print common_items(list1, list2)

    print "Common items 2 (using dictionary):"
    print common_items2(list1, list2)

    print "Sum zero:"
    print sum_zero(list1)

    print "Remove duplicates:"
    print find_duplicates(words)

    print "Word length:"
    word_length("twain.txt")

    pirate()

if __name__ == "__main__":
    main()
