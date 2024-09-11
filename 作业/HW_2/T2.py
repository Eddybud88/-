# 查询
print(dir(list))

# append(x)，向列表的末尾添加一个元素。示例：
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# insert(i, x)，在指定位置 i 插入一个元素 x。示例：
my_list = [1, 3, 4]
my_list.insert(1, 2)
print(my_list)

# remove(x)，移除列表中第一个值为 x 的元素。如果元素不存在，则抛出 ValueError。示例：
my_list = [1, 2, 2, 3]
my_list.remove(2)
print(my_list)

# pop([i])，移除列表中指定位置 i 的元素，并返回它。如果不指定 i，则默认移除并返回最后一个元素。示例：
my_list = [1, 2, 3]
removed_element = my_list.pop(1)
print(my_list)
print(removed_element)

# index(x)，返回列表中第一个值为 x 的元素的索引。如果元素不存在，则抛出 ValueError。示例：
my_list = [1, 2, 3, 4, 3]
index = my_list.index(3)
print(index)

# count(x)，返回列表中元素 x 出现的次数。示例：
my_list = [1, 2, 2, 3, 3, 3]
count = my_list.count(3)
print(count)
