from util import mutate_string

word = input()
data = input().split()

pos = int(data[0])
char = data[1]

result = mutate_string(word, pos, char)
print(result)