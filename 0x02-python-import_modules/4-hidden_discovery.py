#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    allName = dir(hidden_4)
    for name in allName:
        if name[:2] != "__":
            print(name)
