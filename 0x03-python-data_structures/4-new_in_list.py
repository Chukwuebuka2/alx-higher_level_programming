#!/usr/bin/python3
def  new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        if idx == len(my_list):
            my_list[idx - 1] = element
            return my_list
        else:
            my_list[idx] = element
            return my_list


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
