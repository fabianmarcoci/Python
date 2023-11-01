# Exercise 1: Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b, a reunited with b, a - b, b - a)
def operations_on_lists(a, b):
    new_list_of_sets = []
    set_a = set(a)
    set_b = set(b)

    intersection = list(set_a & set_b)
    union = list(set_a | set_b)
    a_not_b = list(set_a - set_b)
    b_not_a = list(set_b - set_a)
    new_list_of_sets.append(intersection)
    new_list_of_sets.append(union)
    new_list_of_sets.append(a_not_b)
    new_list_of_sets.append(b_not_a)
    return new_list_of_sets


def ex1():
    n = int(input("Number of elements for the first list: "))
    m = int(input("Number of elements for the second list: "))
    a = [int(input("Enter element {} of the first list: ".format(i + 1))) for i in range(n)]
    b = [int(input("Enter element {} of the second list: ".format(i + 1))) for i in range(n)]

    new_list_of_sets = operations_on_lists(a, b)
    print(f"a intersected with b: {new_list_of_sets[0]}\na reunited with b: {new_list_of_sets[1]}\n"
          f"a - b: {new_list_of_sets[2]}\nb - a: {new_list_of_sets[3]}")


# --------------------------

# Exercise 2: Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.
def char_occurrences(message):
    char_freq_ratio = {}
    for i in range(len(message)):
        if message[i] in char_freq_ratio:
            char_freq_ratio.update({message[i]: char_freq_ratio.get(message[i]) + 1})
        else:
            char_freq_ratio.update({message[i]: 1})
    return char_freq_ratio


def ex2():
    message = input("Enter the message: ")
    char_freq_ratio = char_occurrences(message)
    print(f'Here is the char - occurrences ratio of the message {message}: {char_freq_ratio}')


# --------------------------

# Exercise 3: Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
'''
class TreeByLevels:
   def __init__(self):
        self.levels = {}
        self.root = None

    def add_node_on_level(self, level, node):
        list_of_nodes = self.levels.get(level, [])
        list_of_nodes.append(node)
        self.levels[level] = list_of_nodes

    def get_nodes_by_level(self, level):
        return self.levels[level]

    class Node:
        def __init__(self, value, level):
            self.level = level
            self.child_nodes = []
            self.value = value
            self.parent = None

        def add_child_node(self, node):
            self.child_nodes.append(node)

        def is_leaf(self):
            return not bool(self.child_nodes)

        def set_parent(self, node):
            self.parent = node

def create_tree(container, level=0, tree=None, parent=None):
    if tree is None:
        tree = TreeByLevels()

    current_node = TreeByLevels.Node(container, level)
    tree.add_node_on_level(level, current_node)

    if parent is None:
        tree.root = current_node
    else:
        current_node.set_parent(parent)

    if isinstance(container, (dict,)):
        for key, value in container.items():
            if isinstance(value, (tuple, set, dict, list)):
                child_node = create_tree(value, level + 1, tree, current_node)
                current_node.add_child_node(child_node)
            else:
                leaf_node = TreeByLevels.Node(value, level + 1)
                tree.add_node_on_level(level + 1, leaf_node)
                current_node.add_child_node(leaf_node)
                leaf_node.set_parent(current_node)


    elif isinstance(container, (list, tuple, set)):
        for element in container:
            if isinstance(element, (tuple, set, dict, list)):
                child_node = create_tree(element, level + 1, tree, current_node)
                current_node.add_child_node(child_node)
            else:
                leaf_node = TreeByLevels.Node(element, level + 1)
                tree.add_node_on_level(level + 1, leaf_node)
                current_node.add_child_node(leaf_node)
                leaf_node.set_parent(current_node)

    return tree

def lists_are_equal(nodes1, nodes2):
    if len(nodes1) != len(nodes2):
        return False

    for node1, node2 in zip(nodes1, nodes2):
        if node1.parent and isinstance(node1.parent.value, (list, set)):
            if node1.value != node2.value or node1.parent.value != node2.parent.value:
                return False
        else:
            if node1.value != node2.value:
                return False

    return True

def compare_trees(tree1, tree2):
    for level in tree1.levels.keys():
        if level not in tree2.levels:
            return False

        nodes1 = tree1.get_nodes_by_level(level)
        nodes2 = tree2.get_nodes_by_level(level)

        if not lists_are_equal(nodes1, nodes2):
            return False
    return True
'''

def compare(dictionary1, dictionary2):
    if len(dictionary1) != len(dictionary2):
        return False

    for key, value in dictionary1.items():

        if key not in dictionary2:
            return False

        if not isinstance(value, type(dictionary2[key])):
            return False

        if isinstance(value, dict):
            if not compare(value, dictionary2[key]):
                return False

        elif isinstance(value, (list, tuple)):
            if len(value) != len(dictionary2[key]):
                return False

            for element1, element2 in zip(value, dictionary2[key]):
                if not isinstance(element1, type(element2)):
                    return False

                if isinstance(element1, (list, tuple, set, dict)):
                    if not compare({"placeholder" : element1}, {"placeholder" : element2}):
                        return False
                else:
                    if element1 != element2:
                        return False

        elif isinstance(value, set):
            sorted_value1 = sorted(list(value))
            sorted_value2 = sorted(list(dictionary2[key]))
            if sorted_value1 != sorted_value2:
                return False

        else:
            if value != dictionary2[key]:
                return False

    return True

def ex3():
    dictionary1 = {
        "a" : 1,
        "b" : 2,
        "c" :[3, 2, 1]
    }
    dictionary2 = {
        "a": 1,
        "b": 2,
        "c": [3, 2, 1]
    }
    '''
    initial_level = 0
    tree1 = create_tree(dictionary1, initial_level)
    tree2 = create_tree(dictionary2, initial_level)
    is_equal = compare_trees(tree1, tree2)
    '''
    is_equal = compare(dictionary1, dictionary2)
    print(f"The equality of the 2 dictionaries is: {is_equal}")

#---------------------------

# Exercise 4: The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element. Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
def build_xml_element(tag, content, **elements):
    attr_str = ''
    for key, value in elements.items():
        attr_str += f' {key}={value}'

    xml_element = f'<{tag}{attr_str}>{content}<{tag}>'
    return xml_element
def ex4():
    print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))

#---------------------------

# Exercise 5: The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.
# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.
def validate_dict(rules, my_dict):
    for key, value in my_dict.items():
        found = False
        for tup in rules:
            if key == tup[0]:
                if value.startswith(tup[1]) and (value.find(tup[2]) and not value.endswith(tup[2])) and value.endswith(tup[3]):
                    found = True
        if not found:
            return False

    return True

def ex5():
    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    my_dict = {
        "key1": "come inside, it's too cold out",
        "key2": "start is middle winter"
    }

    is_valid = validate_dict(rules, my_dict)
    print(f"The validity of the dictionary is: {is_valid}")

#---------------------------

# Exercise 6: Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).
def find_no_unique_elements(my_list):
    set_list = set(my_list)

    duplicate_elements = len(my_list) - len(set_list)
    unique_elements = len(my_list) - duplicate_elements

    return (unique_elements, duplicate_elements)
def ex6():
    my_list = [3, 3, 8, 5, 8, 7, 9]
    unique_elements, duplicate_elements = find_no_unique_elements(my_list)
    print(f"There are {unique_elements} unique elements.\nThere are {duplicate_elements} duplicate elements.")

#---------------------------

# Exercise 7: Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
#
# Ex: {1,2}, {2, 3} =>
#
# {
#
#     "{1, 2} | {2, 3}":  {1, 2, 3},
#
#     "{1, 2} & {2, 3}":  { 2 },
#
#     "{1, 2} - {2, 3}":  { 1 },
#
#     ...
#
# }
def operations_on_sets(*sets):
    operations_dict = {}
    for i in range(len(sets) - 1):
        for j in range(i + 1, len(sets)):
            operations_dict.update({f"{sets[i]} | {sets[j]}": sets[i] | sets[j]})
            operations_dict.update({f"{sets[i]} & {sets[j]}": sets[i] & sets[j]})
            operations_dict.update({f"{sets[i]} - {sets[j]}": sets[i] - sets[j]})
            operations_dict.update({f"{sets[j]} - {sets[i]}": sets[j] - sets[i]})

    return operations_dict

def ex7():
    operations_dict = operations_on_sets({1, 2}, {2, 3}, {2, 4})
    print("These are the operations on our sets:")
    for key, value in operations_dict.items():
        print(f"{key}: {value}")

#---------------------------

# Exercise 8: Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current key is the key for the next value, until you find a loop (a key that was visited before). The function must return the list of objects obtained as previously described.
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']
def loop(mapping):
    key_and_value_objects = [mapping.get("start")]
    count = 0
    freq = {}
    freq.update({mapping.get("start") : 1})
    for index, (key, value) in enumerate(mapping.items()):
        if index == 0:
            continue
        if key_and_value_objects[count] == key:
            if value in freq:
                return key_and_value_objects
            freq.update({value : 1})
            count += 1
            key_and_value_objects.append(value)

    mapping_set = set(mapping)
    return mapping_set

def ex8():
    key_and_value_objects = loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'})
    print(f"Here is a loop: {key_and_value_objects}")

#---------------------------

# Exercise 9: Write a function that receives a variable number of positional arguments and a variable number of keyword arguments adn will return the number of positional arguments whose values can be found among keyword arguments values.
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3
def find_elements(*posargs, **kwargs):
    count = 0
    for arg in posargs:
        for key, value in kwargs.items():
            if arg == value:
                count += 1

    return count
def ex9():
    counter = find_elements(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    print(f"{counter} positional arguments could be found among keyword arguments.")
#---------------------------

if __name__ == '__main__':
    ex1()
    # ex2()
    # ex3() # I left there a bonus attempt commented using trees
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
