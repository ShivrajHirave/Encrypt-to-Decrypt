NormalText = "Python is a very versatile language. It is used in many different types of projects and by many large organizations, including Facebook, NASA, Reddit, and Amazon. Big companies love its power and versatility, so the Python language can be expected to continue to rise in popularity around the world. There's hardly a tech job that you can't apply Python to, which will make you more valuable to any employer or client."
# NormalText = input()                           # User input from console
encrypt = ""

key = "abcdefghijklmnopqrstuvwxyz"

for i in NormalText:
    if i.lower() in key:
        index = key.find(i.lower())
        newindex = (index + 2) % 26
        # newindex = (index - 2) % 26            # Note - Remove this comment to decrypt
        if i.isupper():
            encrypt += key[newindex].upper()
        else:
            encrypt += key[newindex]
    else:
        encrypt += i

print(encrypt)
