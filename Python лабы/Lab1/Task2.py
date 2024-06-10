def main():
    lst = input("Введит list: \n   ")
    lst = lst.split(" ")
    sums_unit = dict()
    max = 0

    for i in range(len(lst)):
        bin_num = bin(int(lst[i]))
        summ = 0
        for j in bin_num: 
            if j != "b":
                summ += int(j)
        sums_unit[i] = summ
        if summ > max:
            max = summ
    sums_unit = dict(sorted(sums_unit.items(), key=lambda x: x[1]))
    #sums_unit = dict(sorted(sums_unit.items(), key=lambda x: (x[1], -x[0])))
    indx = list(sums_unit.keys())
    i=0
    while i < len(indx):
        if i+1 != len(indx):
            if sums_unit[indx[i]] == sums_unit[indx[i+1]]:
                if int(lst[indx[i+1]]) < int(lst[indx[i]]):
                    print(lst[indx[i+1]])
                    print(lst[indx[i]])
                    i += 2
                    continue
                print(lst[indx[i]])
                print(lst[indx[i+1]])
                i += 2
                continue
        print(lst[indx[i]])
        i += 1


main()

