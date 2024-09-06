class Setinfo:
    def __init__(self, initial_set=None):
        self.set_info = set(initial_set) if initial_set else set()

    def add_setinfo(self, keyname):
        self.set_info.add(keyname)

    def get_intersection(self, unioninfo):
        return self.set_info.intersection(unioninfo)

    def get_union(self, unioninfo):
        return self.set_info.union(unioninfo)

    def del_difference(self, unioninfo):
        return self.set_info.difference(unioninfo)

if __name__ == "__main__":
    set1 = Setinfo({1, 2, 3, 4})
    set2 = Setinfo({3, 4, 5, 6})
    set1.add_setinfo(5)
    intersection = set1.get_intersection(set2.set_info)
    union = set1.get_union(set2.set_info)
    difference = set1.del_difference(set2.set_info)
    print("交集:", intersection)
    print("并集:", union)
    print("差集:", difference)
