import random

def AllNames() -> list:
    names_list = []
    with open("names.txt",encoding="utf-8") as file:
        for line in file:
            names_list.append(line[:3])
    return names_list

print("====取名系統====\n\n")

while(True):
    names_list = AllNames()
    first_name = input("輸入您的姓:")
    count = int(input("輸入要的筆數:"))
    random_names = random.choices(names_list,k=count)
    for name in random_names:
        print(first_name + name[-2:])

    繼續 = input("還要繼續?(y,n)")
    if 繼續.lower() == "n":
        break

print("系統結束")