import re

line="Приведение прошуршало и и исчезло в углу."
m1=re.findall("\\ало", line, re.IGNORECASE)
m2=re.findall("\\зло", line, re.IGNORECASE)

print(m1+m2)
