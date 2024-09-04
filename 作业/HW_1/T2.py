"""
replace()方法用于将字符串中的旧子字符串替换为新子字符串，并返回替换后的新字符串
replace()方法也可以替换所有出现的某个字符

find()方法用于查找子字符串在字符串中首次出现的位置（索引），如果未找到则返回 -1

capitalize()方法将字符串的第一个字符转换为大写，其余字符转换为小写
"""

# replace()方法举例
str_example = "Hello, World!"
new_str = str_example.replace("World", "Python")
print(new_str)

str_with_spaces = "Hello    World!"
no_spaces_str = str_with_spaces.replace(" ", "")
print(no_spaces_str)

# find()方法举例
str_example = "Hello, World!"
index = str_example.find("World")
print(index)
not_found_index = str_example.find("Python")
print(not_found_index)

# capitalize()方法举例
str_example = "hello, world!"
capitalized_str = str_example.capitalize()
print(capitalized_str)