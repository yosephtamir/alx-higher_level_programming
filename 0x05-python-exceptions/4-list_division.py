#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    in_list = []
    for i in range(list_length):
        try:
            if my_list_1[i] / my_list_2[i]:
                j = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            j = 0
            print("division by 0")
        except TypeError:
            j = 0
            print("wrong type")
        except IndexError:
            j = 0
            print("out of range")
        finally:
            in_list.append(j)
    return in_list
