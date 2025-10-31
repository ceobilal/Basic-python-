name="hello world"
print(name)

intro= ("Hello My 'friends'")
print(intro)

intro= "hello MY 'chaild'"
print(intro)

intro='"Hello my buddy"'
print(intro)

intro="hello' china"
print(intro)


introduction="""

hello my friends 

How are you 

My name is bilal

i am a software engineer 

"""
print(introduction)


names = '''
ali
bilal
hassain
hasseb
farooq
Adeel
moize
junaid
ramzan
'''
print(names)

# string methods

text="hello world"

print(text.upper())
print(text.lower())
print(text.capitalize())

texts="  Hello friends  "
print(text.strip())     # "hello Python"          (space out) 
print(text.lstrip())    # "hello Python   "     (left space out) 
print(text.rstrip())    # "   hello Python"     (right space out)


Text=" good will "
print(Text.find("will"))    # corect ans na ho to (-1) ho ta hay

print(Text.replace("good","goods"))

print(Text.count("wills"))

print(Text.__add__("goods"))