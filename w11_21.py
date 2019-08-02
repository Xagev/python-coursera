import re
hand = open('sum2.txt')
count=0
for line in hand:
    line = line.rstrip()
    #if re.search('[0-9]+', line) :
        #print(line)

    words=line.split( )
        #print(words)

    for word in words :
        #if re.search('[0-9]+', word) :
        x=re.findall('[0-9]+', word)
        try:
            y = int(x[0])
        except : continue
        #print(y)
        count=count+y
#count=count+3
print(count)
