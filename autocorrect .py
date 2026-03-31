from textblob import TextBlob

text = input("Enter text: ")

corrected = TextBlob(text).correct()

print("Corrected Text:", corrected)
