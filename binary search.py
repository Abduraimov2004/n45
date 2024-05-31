import random


def binar_search() -> None:
    numbers = random.sample(range(1, 100), 30)
    numbers.sort()
    print(numbers)
    target: int = int(input("Qidiriladigan sonni kiriting: "))
    low: int = 0
    lenght = len(numbers) - 1
    count: int = 0
    while low <= lenght:
        mid: int = (low + lenght) // 2
        a: int = numbers[mid]
        print(a)
        count += 1
        if a == target:
            print(f"Siz kiritgan sonni {count} urinishda topdingiz")
            break
        elif a < target:
            low = mid + 1
        else:
            lenght = mid - 1
    else:
        print("Kiritilgan son topilmadi")


def linear_search() -> None:
    print("[1 ___ 30]")
    target = int(input(" son =>"))
    for i in range(1, 31):
        if i == target:
            print(f"""Misol qiymati {target} 
{i}-urinishda topdingiz""")
        else:
            "Misol qiymati topilmadi"


def run() -> None:
    next: str = input("""
    1.> Binary search
    2.> Linear search
            >>>> """)

    if next == '1':
        return binar_search()
    elif next == '2':
        return linear_search()


run()


"""Linear search avzalligi xotiradan kam joy oladi binary searchga qaraganda.
Lekin kotta malumotlar bilan ishlasak Binary searchni qollaganimiz yahshi"""

"""Binary search  algoritmini hosil qilish uchun ma'lumtotlar o'sish tartibida tartiblangan bolshi kerak 
Binary search  algoritmida  int yoki float turidan foydalanish kerak"""