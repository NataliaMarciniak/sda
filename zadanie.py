example = [1, [2, 3, [4, 5]], [[[7]]], 8, [[[[9]]], 10]]
flat_list = []
def flatten_list(old_list):
    for element in old_list:
        if type(element) == list:
            flatten_list(element)
        else:
            flat_list.append(element)


flatten_list(example)
print("Original list: ", example)
print("New list: ", flat_list)