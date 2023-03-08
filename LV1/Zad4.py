words = {}
text = open('song.txt')
for line in text:
    line = line.rstrip()
    line_words = line.split()
    for word in line_words:
        word = word.rstrip(',')
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
text.close()
count = 0
for word in words:
    if words[word] == 1:
        count += 1
        print(word)
print('Number of words that appear once:', count)