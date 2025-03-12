num = int(input())

str = list(input())

result = str
for i in range (num-1):
  com = list(input())
  for j in range (len(str)):
    if (str[j] == com[j]):
      result[j] = str[j]
    else:
      result[j] = "?"

pr = ""
for i in range (len(result)):
  pr += result[i]

print(pr)  