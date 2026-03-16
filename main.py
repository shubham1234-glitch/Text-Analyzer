from analyzer import analyze_text

text = input("Enter your text: ")

clean_words, word_count, most_common_word = analyze_text(text)

print("\nCleaned Words:")
print(clean_words)

print("\nWord Frequency:")
print(word_count)

print("\nMost Frequent Word:", most_common_word)

print("\nUnique Words:", len(word_count))