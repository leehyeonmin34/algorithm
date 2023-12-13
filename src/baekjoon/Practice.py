import re

p = ".*[.][^(bat)]*$"
s = "hi.bat"
s2 = "hi.bar"
print(re.search(p, s))
print(re.search(p, s2))
# print(re.search(p, s).groups())
# print(re.findall(p, s))

# p = re.compile(r'(?P<word>\b\w+\b)')
# m = p.search( '(((( Lots of punctuation )))' )
# print(m.groups())

# print(m.group('word'))
# print(m.groups())
# print(m.group(1))


# p = "([abc])+"
# s = "cba"
# print(re.search(p, s).group()) # cba
# print(re.search(p, s).groups()) # ('a',)
# print(re.findall(p, s)) # ['a']


a = [1,2]
b = [3,4]
[w,x],[y,z] = a, b
print(w,x,y,z)
print([1,2] == [b[0]-2, b[1]-2])