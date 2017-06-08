# 3.2.2

text = "This is my test text. We're keeping this text short to keep things manageable"

def count_words(text):
    """
    count the number of times each word occurs in text (str). Return dictionary where keys are unique words and values are word counts. Skip punctuation
    :param text: 
    :return: 
    """
    text = text.lower()
    skips = [".",",",":",";","'",'"']
    for ch in skips:
        text = text.replace(ch,"")

    word_counts = {}
    for word in text.split(" "):
        # known word
        if word in word_counts:
            word_counts[word] += 1
        # unkknown word
        else:
            word_counts[word] = 1
    return word_counts

count_words(text)


from collections import  Counter
def count_words_fast(text):
    """
    count the number of times each word occurs in text (str). Return dictionary where keys are unique words and values are word counts. Skip punctuation
    :param text: 
    :return: 
    """
    text = text.lower()
    skips = [".",",",":",";","'",'"']
    for ch in skips:
        text = text.replace(ch,"")

    word_counts = Counter(text.split(" "))
    return word_counts

count_words_fast(text)

count_words(text) == count_words_fast(text)


len(count_words("This comprehension check is to check for comprehension."))

# 3.2.3

def read_book(title_path):
    """
    Read a book and return it as a string
    :param title_path: 
    :return: 
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

text = read_book('C:/Users/Charl/PycharmProjects/PH526x/books/English/shakespeare/Romeo and Juliet.txt')

len(text)

ind = text.find("What's in a name")
ind

sample_text = text[ind: ind + 1000]
sample_text

# 3.2.4

def word_stats(word_counts):
    """
    Return number of unique words and frequencies
    :param word_counts: 
    :return: 
    """
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

text = read_book('C:/Users/Charl/PycharmProjects/PH526x/books/English/shakespeare/Romeo and Juliet.txt')

word_counts = count_words(text)

(num_unique, counts) = word_stats(word_counts)

num_unique
sum(counts)

text = read_book('C:/Users/Charl/PycharmProjects/PH526x/books/English/shakespeare/Romeo and Juliet.txt')
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))

text = read_book('C:/Users/Charl/PycharmProjects/PH526x/books/German/shakespeare/Romeo und Julia.txt')
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))


# 3.2.4

import os
bood_dir = "./books"

import pandas as pd
stats = pd.DataFrame(columns=("language", "author","title","length", "unique"))
title_num = 1

os.listdir(bood_dir)

for language in os.listdir(bood_dir):
    for author in os.listdir(bood_dir + "/" + language):
        for title in os.listdir(bood_dir + "/" + language + "/" + author):
            input_file = bood_dir + "/" + language + "/" + author + "/" + title
            print(input_file)
            text = read_book(input_file)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language,author.capitalize(),title.replace(".txt",""),sum(counts),num_unique
            title_num += 1



stats
stats.head()
stats.tail()
import pandas as pd



table = pd.DataFrame(columns = ("name", "age"))

table.loc[1] = "James", 22
table.loc[2] = "Jess", 32

table
table.columns

# 3.2.6

stats.length
stats.unique

import matplotlib.pyplot as plt
plt.plot(stats.length, stats.unique, "bo")
plt.show()

plt.loglog(stats.length, stats.unique, "bo")
plt.show()

stats[stats.language == "English"]
stats[stats.language == "French"]

plt.figure(figsize=(10,10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label = "French", color = "forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label = "German", color = "orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label = "Portuguese", color = "blueviolet")
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of unique words")
plt.savefig("langplot.png")
