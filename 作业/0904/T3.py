L1 = ["Oasis", "Blur", "Suede", "Fix", "Kinks"]
L2 = ["Zeppelin", "Queen", "Oasis", "Kinks", "Beatles"]

common_elements = [element for element in L1 if element in L2]

unique_to_L1 = [element for element in L1 if element not in L2]

positions_in_L2 = {element: L2.index(element) for element in L1 if element in L2}

print("L1和L2的共同元素:", common_elements)
print("L1中特有的元素:", unique_to_L1)
print("L1中的元素在L2中的位置:", positions_in_L2)
