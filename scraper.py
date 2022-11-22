import requests
from bs4 import BeautifulSoup
import sumfromoutput

url_list = []

for i in range(1, 20):
    url_list.append('https://scp-wiki.wikidot.com/scp-' + str('{0:0>3}'.format(i)))

# the_word = input()
the_word = 'keter'
total = 0

total_words = []
for url in url_list:
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content.lower(), 'lxml')
    words = soup.find_all(text=lambda text: text and the_word.lower() in text)
    count = len(words)
    words_list = [ele.strip() for ele in words]
    for word in words:
        total_words.append(word.strip())
        if the_word:
            total += 1

    print('\nUrl: {}\ncontains {} of word: {}'.format(url, count, the_word))
    print(words_list)

with open("output.txt", "a", encoding='utf-8') as f:
    print(total_words, file=f)
    print("total words: " + str(total), file=f)

total_count = len(total_words)
sumfromoutput.count()

