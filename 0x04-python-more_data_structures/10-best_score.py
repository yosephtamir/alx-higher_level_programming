#!usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for i in a_dictionary.items():
            temp = i[1]
            maxim = i[0]
        for i in a_dictionary.items():
            if i[1] > temp:
                temp = i[1]
                maxim = i[0]
        return maxim
    else:
        return None
