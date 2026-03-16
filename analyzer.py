def analyze_text(text): 

    text = text.lower()

    words = text.split()

    stop_words = ["is", "the", "and", "of", "to", "in", "a"]

    word_count = {}

    clean_words = []

    for word in words:

        if word in stop_words:
            continue

        clean_words.append(word)

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_common_word = ""
    max_count = 0

    for word, count in word_count.items():

        if count > max_count:
            max_count = count
            most_common_word = word

    return clean_words, word_count, most_common_word