from random import randint,choice
from ipaddress import IPv4Network
import csv
import os
import re

MASK = "mask.log"
IP_ADDR = "ip_solve.log"
STORE = "store.csv"
CATEGORIES = "categories.csv"
ARTICLE_SOLVE = "article_solve.txt"
ARTICLE = "article.txt"

def generate_mask():
    mask = IPv4Network((0,randint(0,32)),strict=False)
    return str(mask.netmask)

def task1():
    try:
        with open(MASK,"w",) as mask_file:
            for i in range(20):
                mask = generate_mask()
                mask_file.write(mask+"\n")
        print("Task 1 completed !")
    except Exception as Ex:
        print(Ex)

def apply_mask(ip,mask):
    network = IPv4Network(ip+"/"+mask,strict=False)
    return str(network.network_address)

def task2():
    ip_addr = input("Введите ip адрес:\n")
    with open(MASK,"r+") as mask_file:
        masks = mask_file.readlines()
        for mask in masks: 
            mask = mask.replace("\n","")
            with open(IP_ADDR,"a+") as ip_file:
                ip_file.write(apply_mask(ip_addr,mask)+"\n")
    print("Task 2 completed !")

def task3():
    with open(STORE,"r+",encoding="utf-8",newline="") as products_file:
        products = csv.reader(products_file)
        categories = dict()
        for product in products:
            product[0] = product[0].split(";")
            if product[0][1] in "Категория":
                categories[product[0][1]] = product[0][2]
                continue
            if product[0][1] in categories:
                categories[product[0][1]] += float(product[0][2])
                continue
            categories[product[0][1]] = float(product[0][2])
    print(categories)
    categories_list = list(categories)
    with open(CATEGORIES,"a+",encoding="utf-8",newline="") as categories_file:
        writer = csv.writer(categories_file,delimiter=";")
        for i in categories_list:
            writer.writerow([i,categories[i]])
    print("Task 3 completed !")

def task4():
    project_dir = os.path.dirname(os.path.abspath(__file__))#определение нынешней директории
    example_dir = os.path.join(project_dir, 'example')#путь до папки
    extensions = ['.txt', '.py', '.jpg', '.csv', '.xml', '.json', '.html', '.css', '.js', '.pdf', '.doc']

    if not os.path.exists(example_dir):
        os.mkdir(example_dir)#создание папки

    for i in range(100):
        rand_ext = choice(extensions)
        filename = f'my_file{i}{rand_ext}'
        file_path = os.path.join(example_dir, filename)
        
        open(file_path, 'a').close()

def task5():
    file_type = input("Введите расширение файла: ")
    project_dir = os.path.dirname(os.path.abspath(__file__))
    example_dir =  os.path.join(project_dir, 'example')
    count = 0
    for filename in os.listdir(example_dir):
        if filename.endswith(file_type):
            count += 1

    print(f"Количество файлов с расширением {file_type}: {count}")
    
def task6():
    with open(ARTICLE,"a+", encoding='utf-8') as f:
        text = f.read()


    text = re.sub(r'[^а-яA-Za-zА-Яа-я]', ' ', text).lower()# Удаление всех за исключением букв русского и английского алфавитов  

    # Подсчитываем частоту каждой буквы
    counts = {}
    for letter in text:
        counts[letter] = counts.get(letter, 0) + 1

    # Вычисляем частоту в долях
    total = sum(counts.values()) 
    for letter in counts:
        counts[letter] = counts[letter] / total
    letters = sorted(counts, key=counts.get, reverse=True)

    with open(ARTICLE_SOLVE, 'w', encoding='utf-8') as f:
        for letter in letters:
            f.write(f'{letter}: {counts[letter]:.3f}\n')

def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()

main()