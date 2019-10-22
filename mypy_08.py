# Dictionaries
post = {"user_id":938, "message":"Hello Python", "language":"English", "location":"Sydney"}
print(post)

print()

print(post.keys())

print()

for key in post.keys():
    print(key,'=',post[key])

print()

for key,value in post.items():
    print(key,'=',value)

print()

post.pop("language")
print(post)