from bs4 import BeautifulSoup
import requests

def getHtml():
    """
    This function prompts the user for a link, fetches the HTML content of the page.
    """
    while True:
        link = input("Enter the link: ")
        r = requests.get(link)
        if r.status_code != 200:
            print("Error: Unable to access the link.")
            continue
        return BeautifulSoup(r.text, 'html.parser')
    
def freqWordCounter(page):
    """
    This function counts the frequency of 30 words in the HTML content,
    ignoring words with length less than or equal to 3.
    """
    text = page.get_text()
    for i in ".,!?:;()[]{}<>-_\"'+`~@#$%^&*|\\/": text = text.replace(i, "")
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if len(word) <= 3: continue
        if word not in word_count: word_count[word] = 1
        else: word_count[word] += 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    print("Most frequent words:")
    for idx, (word, count) in enumerate(sorted_word_count[:30], 1):
        print(f"\t{idx}. {word}: {count}")

def freqTegCounter(page):
    """
    This function counts the frequency of tags in the HTML content.
    """
    tags = page.find_all()
    tag_count = {}
    for tag in tags:
        tag_name = tag.name
        if tag_name not in tag_count: tag_count[tag_name] = 1
        else: tag_count[tag_name] += 1

    sorted_tag_count = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
    print("Most frequent tags:")
    for idx, (tag, count) in enumerate(sorted_tag_count, 1):
        print(f"\t{idx}. {tag}: {count}")

def Amount(page, tag):
    """
    This function counts the number of occurrences of a specific tag in the HTML content.
    """
    tags = page.find_all(tag)
    return len(tags)

def loop():
    """
    This function runs the main loop of the program.
    """
    while True:
        page = getHtml()
        print("Page title:", page.title.string)
        freqWordCounter(page)
        freqTegCounter(page)
        print("Number of links:", Amount(page, 'a'))
        print("Number of images:", Amount(page, 'img'))
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y': break