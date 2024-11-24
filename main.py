import string

# 1. Change the encoding to utf-8 for simpler characters
text = open("read.txt", encoding="utf-8").read()

# 2. convert all characters to lowercase
lowerCase = text.lower()

# 3. Remove punctuations such as ! and ?.

# ---------------- content of the 'translate' method _____________________
# str1: specifies the list of characters that need to be replaced
# str2: specifies the list of characters with which the characters need to be replaced
# str3: specifies the list of characters that needs to be deleted
clean_text = lowerCase.translate(str.maketrans('', '', string.punctuation))

# store each character on a list (tokenize)
tokenized_words = clean_text.split()
# print(tokenized_words)

# list of stop words, which are words that doesn't add any emotional meaning to a sentence
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# the final_words list for storing the final words to be processed
final_words = []
# removing stop words for our list
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

print(final_words)


# NLP Emotion Algorithm
# 1) check if word in the final words list is also present in emotion.txt
#    - Open the emotion file.
#    - Loop through each line and clear it.
#    - Extract the word and emotion using split

# 2) if word is present -> add emotion to emotion_list
# 3) Finally count each emotion in the emotion_list
