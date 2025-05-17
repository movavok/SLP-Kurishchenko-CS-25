from numpy import *
import matplotlib.pyplot as plt

def showFunPlot(t, y):
    """
    Function to plot the function y = cos(t^2)/t
    :param t: array of t values
    :param y: function values
    :return: None
    """
    plt.plot(t, y, 'r-', label='cos(t^2)/t')
    plt.plot(t, y, 'k*', label='data points')    
    plt.axis([0, 5, -1, 10])
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('First task plot')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('../Plots/firstTaskPlot.png', dpi=200)
    plt.show()

def autoLoad(fileName, text):
    """
    Function to load text from a file if the input is '1'
    :param fileName: name of the file to load
    :param text: input text
    :return: text
    """
    if text.strip() == "1":
        with open(fileName, 'r', encoding="utf-8") as file:
            text = file.read()
    return text

def showLetterFreqPlot(text):
    """
    Function to plot the frequency of letters in a text
    :param text: input text
    :return: None
    """
    text = autoLoad("test_sentence.txt", text).lower()
    freq = {}
    for letter in text:
        if letter.isalpha():
            freq[letter] = freq.get(letter, 0) + 1
    letters = list(freq.keys())
    counts = list(freq.values())
    
    plt.bar(letters, counts)
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency')
    plt.tight_layout()
    plt.savefig('../Plots/secondTaskPlot.png', dpi=200)
    plt.show()

def showSenTypesPlot(text):
    """
    Function to plot the frequency of sentence types in a text
    :param text: input text
    :return: None
    """
    text = autoLoad("test_sentence.txt", text).lower()
    counts = {'.': 0, '?': 0, '!': 0, '...': 0}

    i = 0
    n = len(text)
    while i < n:
        if text[i:i+3] == '...':
            counts['...'] += 1
            i += 3
        elif text[i] in '.!?':
            counts[text[i]] += 1
            i += 1
        else: i += 1

    labels = [k for k in counts if counts[k] > 0]
    values = [counts[k] for k in labels]

    plt.bar(labels, values, color=['gray', 'blue', 'red', 'magenta'][:len(labels)])
    plt.xlabel('Sequence Type')
    plt.ylabel('Count')
    plt.title('Punctuation Sequence Types Frequency')
    plt.tight_layout()
    plt.savefig('../Plots/thirdTaskPlot.png', dpi=200)
    plt.show()


def run():
    """
    Main function to run the program
    :return: None
    """
    t = linspace(0, 5, 51)
    y = cos(t**2) / t
    showFunPlot(t, y)
    showLetterFreqPlot(input("Enter a text to count letter frequency (enter 1 to auto): "))
    showSenTypesPlot(input("Enter a text to count sentence types (enter 1 to auto): "))