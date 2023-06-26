#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    for func in dir(hidden_4):
        if func[:2] == "__":
            continue
        print(func)
