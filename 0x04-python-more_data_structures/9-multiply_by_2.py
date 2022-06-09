#!/usr/bin/python3

<<<<<<< HEAD
def multiply_by_2(a_dictonary):
    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v * 2
    return new_dict
=======
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *= 2

    return (new_dir)
>>>>>>> ce89200cf259a66cac54fec9a2433c09ce3201d0


if __name__ == "__main__":
    multiply_by_2(a_dictionary)
