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
def count_unique(string1):
    d = {}
    letter_count = {}
    word_list = string1.split()
    for word in word_list:
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
    pass

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
    count_unique(string1)

    print "Common items:"
    print common_items(list1, list2)

    print "Common items 2 (using dictionary):"
    print common_items2(list1, list2)

    print "Sum zero:"
    print sum_zero(list1)

    print "Remove duplicates:"
    print find_duplicates(words)

if __name__ == "__main__":
    main()
