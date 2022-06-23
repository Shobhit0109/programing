a = "hey my name is"

b = []

c = ""
for i in a + ' ':
	if i == ' ':
		b.append(c)
		c = ""
		continue
	c += i

print(b)