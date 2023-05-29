#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    in_list = []
    try:
        for i in range(list_length):
            try:
                if my_list_1[i] / my_list_2[i]:
                    in_list.append(my_list_1[i]/my_list_2[i])
            except ZeroDivisionError:
                in_list.append(0)
                print("division by 0")
            except TypeError:
                in_list.append(0)
                print("wrong type")
            except IndexError:
                in_list.append(0)
                print("out of range")
    except Exception:
        pass
    finally:
        return in_list
