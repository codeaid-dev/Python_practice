import random
import string
def randomword1(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

def randomword2(length):
    x = ""
    for i in range(length):
        x = x + random.choice(string.ascii_lowercase)
    return x

# returns a 10 character long string by calling function v1
randomString1 = randomword1(10)
# returns a 15 character long string by calling function v2
randomString2 = randomword2(15)

def randomword3(length):
    s = ""
    #random.seed(1)
    while len(s) < length:
        r = random.randint(0, len(string.ascii_lowercase)-1)
        s += string.ascii_lowercase[r]
    return s

print(randomString1)
print(randomString2)

randomString3 = randomword3(13)
print(randomString3)
