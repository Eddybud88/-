example_dict = {'a': 1, 'b': 2, 'c': 3}

"""
clear: 清空字典
copy: 返回字典的一个浅拷贝
fromkeys: 创建一个新字典，以序列seq中的元素作为键，值为value
get: 返回指定键的值，如果键不存在则返回默认值
items: 返回字典中的键值对列表
pop: 移除指定键的项，并返回其值。如果键不存在，则返回默认值
"""

example_dict.clear()
print("清空后的字典:", example_dict)

# 重新初始化示例字典
example_dict = {'a': 1, 'b': 2, 'c': 3}

copy_dict = example_dict.copy()
print("浅拷贝后的字典:", copy_dict)

new_dict = dict.fromkeys(['a', 'b', 'c'], 100)
print("新创建的字典:", new_dict)

value = example_dict.get('d', 'Not Found')
print("获取键'd'的值:", value)

items_list = example_dict.items()
print("返回键值对列表:", items_list)

popped_value = example_dict.pop('b', 'Not Found')
print("移除并返回键'b'的值:", popped_value)
print("字典现在为:", example_dict)
