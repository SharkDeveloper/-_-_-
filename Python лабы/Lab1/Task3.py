import datetime

def main():
    n = input("Введите n:\n     ")
    user = str()
    login = str()
    dt = dict()
    users = dict()
    ip = set()
    dt_list = list() #list with dict dt
    count = dict()

    for i in range(int(n)):
        user = input()
        user = user.split(" ")
        login = user[0]

        if not(login in users.keys()):
            count[login] = 1
            ip = set()
            ip.add(user[2])
            dt = {}
            dt[user[1]] = ip
            users[login]= dt
            continue

        if not(user[1] in dt.keys()):
            count[login] = 1
            ip = set()
            ip.add(user[2])
            dt[user[1]] = ip
            users[login]= dt
            continue

        ip.add(user[2])
        dt[user[1]] = ip
        users[login]= dt

        count[login] += 1


    count = list(dict(sorted(count.items(), key=lambda x: x[1])).keys())

    print("Логин:",count[-1])


main()

    

    