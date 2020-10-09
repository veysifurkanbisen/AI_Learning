"""
BTK - Dersleri

6.6 - Döngü Methodları (range(), enumerate())
6.7 - Pythonda List (Comprehensions)
6.8 - Sayı Tahmin Uygulaması
6.9 - Asal Sayı Uygulaması
7.1 - Pythonda Methodlar
7.2 - Fonksiyon Kullanımı
7.3 - Fonksiyon Parametreleri
7.4 - Uygulama-Fonksiyonlar
"""

import random

# for x in range(3):
#     for y in range(3):
#         for z in range(3):
#             # print(x, y)
#             pass
#
# cls = [print(x, y) for x in range(3) for y in range(3)]
# print(cls)

"""
##### Sayı Tahmin Uygulaması #####

1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
** "random" modülünü kullanın.
** 100 üzerinden puanlama sistemi yapın. Her soru 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""


def predict():
    try:
        target = random.randint(0, 101)
        print(target)
        turn = int(input("Please state how many rounds you would like to start with: "))
        score = 100
        point = int(score/turn)
        for i in range(turn):
            print("You have", turn, "turns left.")
            answer = int(input("Make prediction between 0-100: "))
            if answer < target:
                score -= point
                turn -= 1
                print("Too low!\n")
            if answer > target:
                score -= point
                turn -= 1
                print("Too high!\n")
            if answer == target:
                print("Congrats... You Win!")
                print("Your score:", score)
                break
        if turn == 0:
            print("Boomer... You LOST!\nCorrect number was:", target)
    except ValueError:
        print("Please write number not 'text'!")


# Uncomment below line to run the program
# predict()


"""
##### Asal Sayı Uygulaması #####

Girilen bir sayının asal sayı olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam bölüneni olmayan sayılara denir.
"""


def is_prime():
    try:
        number = int(input("Give a number to check: "))
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    print(number, "is not a prime number")
                    print(i, "times", number // i, "is", number)
                    break
            else:
                print(number, "is a prime number")
        else:
            print(number, "is not a prime number")
    except ValueError:
        print("Give a number as input not 'string'!")


# Uncomment below line to run the program
# is_prime()

"""
##### Fonksiyon Uygulama #####

# 1 - Gönderilen birkelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
# 2 - Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.
# 3 - Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
# 4 - Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazın.
"""


# -1.1-
def repeat1(name):
    print("Running function is repeat1")
    try:
        repeat_time = int(input("Please give the number of times you would like to see the word: "))
        i = 0
        while repeat_time > i:
            print(str(repeat_time) + ". " + "time." + name)
            repeat_time -= 1
    except ValueError:
        print("Please give number not 'string'!")


# -1.2-
def repeat2(word, times):
    print("Running function is repeat2")
    while times > 0:
        print(str(times) + ". " + word)
        times -= 1


# -1.3-
def repeat3():
    print("Running function is repeat3")
    try:
        word = input("Give the name: ")
        times = int(input("Give repeat time: "))
        while times > 0:
            print(str(times) + ". " + word)
            times -= 1
    except ValueError:
        print("Please give number not 'string'!")


# Uncomment one of the below lines to run the program 1.1, 1.2 or 1.3
# repeat1("veysi")
# repeat2("veysi", 3)
# repeat3()


# -2-
def create_list(*args):
    return list(args)
# Uncomment below line to run the program
# print(create_list(1, 2, 3, 4, 5, 6, 7))


# -3-
def find_prime(num1, num2):
    print("Running function is 'find_prime'")
    # num2 mus be greater than num1
    # num1 must be greater than 1
    prime_numbers = []
    for number in range(num1, num2+1):
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            prime_numbers.append(number)

    return prime_numbers
# Uncomment below line to run the program
# print(find_prime(2, 100))


# -4-
def aliquot(number):
    aliquot_numbers = []
    for divider in range(1, number + 1):
        if number % divider == 0:
            aliquot_numbers.append(divider)
    return aliquot_numbers
# Uncomment below line to run the program
# print(aliquot(20))
