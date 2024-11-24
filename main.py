import string

# 1. Change the encoding to utf-8 for simpler characters
text = open("read.txt", encoding="utf-8").read()

# 2. convert all characters to lowercase
lowerCase = text.lower()

# 3. Remove punctuations such as ! and ?.

# ----------------
# str1: specifies the list of characters that need to be replaced
# str2: specifies the list of characters with which the characters need to be replaced
# str3: specifies the list of characters that needs to be deleted

clean_text = lowerCase.translate(str.maketrans('', '', string.punctuation))
print(clean_text)