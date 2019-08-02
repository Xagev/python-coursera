str = 'X-DSPAM-Confidence:0.8475'
print(str)
colon=str.find(':')
print(colon+1)
colon=colon+1
print(str[colon:])
number=float(str[colon:])
print(number)
