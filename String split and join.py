def split_and_join(line):
    # write your code here
    splitted = line.split()
    return "-".join(splitted)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
