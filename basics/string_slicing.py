#slicing[start:stop:step]

name = "Daylan Pravir Maharaj"

substring = name[0:6]
print(substring)
substring = name[::2]
reversed_name = name[::-1]
print(substring)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slices = slice(7,-4)
print(website1[slices])
print(website2[slices])