import random
import string

length = input("Enter password length: ")
pwfile = open("password.txt", "r+")

pw = ''

def generate():
    generate.char = random.choice(string.ascii_letters)
    generate.punc = random.choice(string.punctuation)
    generate.num = str(random.randint(1, 300))


for i in range(int(length)):
    generate()
    pw = generate.char + generate.punc + generate.num + pw

print("Generation finished, your password: " + pw)
savepw = input("Save password in .txt file? (Y/N)")

if savepw == "Y":
    pwfile.write("PASSWORD: " + pw)
    pwfile.close
else:
    exit()