
def sort_list(numbers):
    passed_list = []
    for element in numbers:
        if isinstance(element, int):
            passed_list.append(element)
        else:
            if isinstance(element, str):
                continue
            elif isinstance(element, list):
                for x in element:
                    if isinstance(x, int):
                        passed_list.append(x)
                    elif isinstance(x, str):
                        continue
                    elif isinstance(x, list):
                        for y in x:
                            if isinstance(y, int):
                                passed_list.append(y)
                            elif isinstance(y, str):
                                continue
    return passed_list

example = [1, [2, 3, [4, 5]], 7, 8, [[9], 10]]
print("Original list: ", example)
print("New list: ", sort_list(example))