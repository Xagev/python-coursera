fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

counts = dict()

for line in fh:
    if not line.startswith('From') : continue
    words=line.split()
    #print(words)
    try:
    	mail=words[5]
    except: continue
    hour=mail[0:2]
    #print(hour)
    counts[hour]=counts.get(hour,0)+1

#print(counts)
c=sorted( counts.items() )
for a,b in c:
    #a=int(a)
    print(a,b)
