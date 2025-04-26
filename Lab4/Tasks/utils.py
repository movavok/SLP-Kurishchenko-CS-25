def listOfWords():
    """
    Повертає три списки: прикметники, іменники та дієслова.
    """
    adjectives = [
        "сонний", "пухкий", "обурений", "шумний", "підозрілий",
        "засмаглий", "втомлений", "мокрий", "блискучий", "невидимий",
        "лінивий", "скажений", "гордий", "істеричний", "жирний",
        "волохатий", "кисленький", "розгублений", "рогатий", "меланхолійний"
    ]
    nouns = [
        "кабан", "банан", "робот", "холодильник", "пельмень",
        "йогурт", "носоріг", "чайник", "бобер", "папуга",
        "тюлень", "вентилятор", "інопланетянин", "гарбуз", "дурник",
        "пінгвін", "буряк", "котлета", "кактус", "мікрохвильовка"
    ]
    verbs = [
        "стрибає", "пливе", "гавкає", "мурчить", "кричить",
        "ховається", "танцює", "зникає", "засинає", "чекає",
        "здіймається", "тупцяє", "регоче", "блимає", "зависає",
        "перевтілюється", "жонглює", "скаче", "витріщається", "вибухає"
    ]
    return adjectives, nouns, verbs

def genRanSentence(adjectives, nouns, verbs):
    """
    Генерує випадкове речення з трьох частин: прикметник, іменник, дієслово.
    """
    import random
    print("Завдання 1. Твоя випадкова фраза:", f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}")

def amountOfSymbols(filePath):
    """
    Повертає кількість символів у текстовому файлі.
    """
    with open(filePath, "r", encoding='utf-8') as file:
        text = file.read()
        print("Завдання 2.1) Кількість символів у файлі(з пробілами):  ", len(text))
        print("              Кількість символів у файлі(без пробілів): ", len(text.replace(" ", "")))

def getCleanedWords(filePath):
        """
        Зчитує текстовий файл, очищає текст від розділових знаків і повертає список слів.
        """
        with open(filePath, "r", encoding='utf-8') as file:
            text = file.read()
            cleaned_text = text.replace(".",
                           " ").replace(",", 
                           " ").replace("-", 
                           " ").replace("!", 
                           " ").replace("?", 
                           " ").replace("—", 
                           " ").replace(":", 
                           " ").replace(";", " ")
            words = cleaned_text.split()
        return words

def amountOfWords(filePath):
    """
    Повертає кількість слів у текстовому файлі.
    """
    words = getCleanedWords(filePath)
    print("           2) Кількість слів у файлі:               ", len(words))
    different_words = set(word.lower() for word in words)
    print("              Кількість різних слів(без повторів):  ", len(different_words))
    word_counts = {}
    for word in words:
        word_lower = word.lower()
        word_counts[word_lower] = word_counts.get(word_lower, 0) + 1
    unique_words = [word for word, count in word_counts.items() if count == 1]
    print("              Кількість унікальних слів у файлі:    ", len(unique_words))

def findRepSeq(filePath):
    """
    Повертає найдовшу повторювану послідовність слів у текстовому файлі.
    """
    words = words = getCleanedWords(filePath)
        
    longest_seq = []
    max_length = 0
        
    for length in range(2, min(11, len(words))):
        sequences = {}
            
        for i in range(len(words) - length + 1):
            seq = tuple(words[i:i + length])
            sequences[seq] = sequences.get(seq, 0) + 1
            if sequences[seq] > 1 and length > max_length:
                longest_seq = seq
                max_length = length
        
    if longest_seq:
        print("Завдання 3. Найдовша повторювана послідовність слів:", " ".join(longest_seq))
    else:
        print("Завдання 3. Повторюваних послідовностей не знайдено")




