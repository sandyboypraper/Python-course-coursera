text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
x = text[pos:]
y = float(x)
print(y)
