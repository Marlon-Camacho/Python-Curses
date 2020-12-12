text = "X-DSPAM-Confidence:    0.8475"
t = text.find('0')
tr = float(text[t:])
print(tr)
