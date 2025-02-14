avgltr = 0
avgsent = 0
lttrlen = 0
phrase = input("Text: ")
words = phrase.split()
sentences = phrase.count(".") + phrase.count("!") + phrase.count("?")
for i in phrase:
    if i.isalpha():
        lttrlen += 1
avgltr = lttrlen/len(words)
avgltr *= 100
avgsent = (sentences / len(words)) * 100
reading_lvl = 0.0588 * avgltr - 0.296 * avgsent - 15.8
if reading_lvl < 1:
    print("Before Grade 1")
elif reading_lvl >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(reading_lvl)}")