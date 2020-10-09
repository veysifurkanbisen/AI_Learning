"""
BTK - Dersleri

7.5 - Lambda Expressions, Map, Filter
7.6 - Fonksiyonların Kapsamı - Global ve Yerel Değişkenler
7.7 - Bankamatik Uygulaması
"""
numbers = [1, 3, 5, 9]

# Map
def square(num): return num ** 2


square_1 = lambda num: num ** 2

map_result_1 = list(map(square, numbers))
map_result_2 = list(map(lambda num: num ** 2, numbers))
map_result_3 = square_1(3)


# Filter
def check_even(num): return num % 2 == 0

check_even_1 = lambda num: num **3

filter_result_1 = list(filter(check_even, numbers))
filter_result_2 = list(filter(lambda num: num ** 2, numbers))
filter_result_3 = check_even_1(3)

