import urllib.request, json

address = input('Enter location: ')
with urllib.request.urlopen(address) as url:
    data = json.loads(url.read().decode())
    print(data)
lets0=(json.dumps(data, indent=4))
sum=0
lets=data['comments']
for line in lets :
    #print(line['count'])
    sum=sum+line['count']

print(sum)
