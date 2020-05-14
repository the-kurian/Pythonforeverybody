text = "X-DSPAM-Confidence:    0.8475";
v=text.find('0')
data= text[v:]
x=float(data)
print(x)
