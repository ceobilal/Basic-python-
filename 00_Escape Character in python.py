Esacp_Seqence_character="""
hello\nworld   
hello\tworld
hello\"world
hello\"world\"
hello\'world
hello\'world\'
hello\\world
hello\\world\\
"""
print(Esacp_Seqence_character)

a="hello\nworld"       # line break 
b="hello\tworld"       # tab space  (hello   world)
c="hello\"world"       #  (hello"world)
d="hello\"world\""     #  hello"world")
e="hello\'world"       # (hello'world)
f="hello\'world\'"     # (hello'world')
g="hello\\world"       # hello\world 
h="hello\\world\\"     # hello\world\

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

print(a) ; print(b) ; print(c) ; print(d) ; print(e) ; print(f) ; print(g) ; print(h)

print(a,b,c,d,e,f,g,h)