# create file and write on it
f = open("file.txt", "w")
f.write("Python Course \n")
f.write("Deep Learning Course")
f.close()

# open and read the file after the appending:
f = open("file.txt", "r")
wordcount = {}
for w in f.read().split():
    if w in wordcount:
        wordcount[w] += 1
    else:
        wordcount[w] = 1


for key, value in wordcount.items():
    print(key, value)
    f = open("file.txt", "a")
    f.write("%s %i\n" % (key, value))




