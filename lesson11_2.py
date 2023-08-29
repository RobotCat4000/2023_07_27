import random
def 獲得分數() -> list:
    分數 = []
    for i in range(5):
        分數.append(random.randint(50, 100))
    return 分數

def get_names(nums:int) -> list:
    with open('names.txt',encoding='utf-8',newline='') as file:
        names_str = file.read()
        All_names_list = names_str.split(sep="\n")
        names_list = random.choices(All_names_list,k=數量_int)#取出一定數量的姓名
    return names_list

數量_int = int(input("輸入學生數:"))#取得(輸入數量)個姓名
names_list = get_names(數量_int)
學生 = []
for i in range(數量_int):
    分數 = 獲得分數()
    New_list = [names_list[i]] + 分數
    學生.append(New_list)
print(學生)