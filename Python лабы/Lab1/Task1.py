
def check_equal(str: str):
    start = str[:(len(str)//2)]
    end = str[(len(str)//2):]
    end = end[::-1]
    if len(end) > len(start):
        end = end[1:]
    if start == end:
        return 1

def main():
    str = input("Введите строку s: \n     ")
    str = str.lower()
    indexes = list()
    for i in range(len(str)):
        palindrom = str[:i]+str[i+1:]
        if check_equal(palindrom):
            indexes.append(i)
    print("Колличество индексов n =",len(indexes))

main()