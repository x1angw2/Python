def worlds(input):
    worlds = input.split(" ")
    worlds = worlds[-1::-1]
    out = ' '.join(worlds)
    return out
if __name__ == "__main__":
    input = input("输入字符串")
    rw = worlds(input)
    print(rw)
