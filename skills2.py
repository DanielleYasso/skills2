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
def strip_words(word_list, d, letter_count):
    for word in word_list:
        word = word.strip(" .!?,;:-_\"'*()[]")
        if "--" in word:
            more_words = word.split("--")
            strip_words(more_words, d, letter_count)
        else:
            d[word] = d.get(word, 0) + 1
            for letter in word:
                letter_count[letter] = letter_count.get(letter, 0) + 1
    # remove empty string            
    if d.get("", 0) == 276:
        del d[""]
    return d, letter_count

def count_unique(string1):
    d = {}
    letter_count = {}
    f = open(string1)
    for line in f:
        word_list = line.strip().split()
        d, letter_count = strip_words(word_list, d, letter_count)
        
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
        if list2.__contains__(item):
            if common_list.__contains__(item):
                continue
            else:
                common_list.append(item)

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
"""
def sum_zero(list1):
    zero_sums = []
    for num in list1:
        for num2 in list1:
            if num + num2 == 0:
                zero_sums.append((num, num2))
    return zero_sums


"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    words_set = set(words)
    words_list = list(words_set)
    return words_list

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    d = {}
    for word in words:
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
    word_length(words)

if __name__ == "__main__":
    main()
