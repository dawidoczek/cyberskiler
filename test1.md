<details>
<summary>A) Definiowanie funkcji</summary>
<ul>
<details>
<summary>1. Pierwsza funkcja:</summary>
```python
def greetings():
    print("Hello, this is function.")

if __name__ == "__main__":
    greetings()
```
</details>
<details>
<summary>2. Ciąg Fibonacciego:</summary>
```python
def print_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
    print(" ".join(map(str, fib_sequence[:n])))

if __name__ == "__main__":
    n = int(input())
    print_fibonacci_sequence(n)
```
</details>
<details>
<summary>3. Funkcja sumująca liczby:</summary>
```python
def sum(a, b):
    print(a + b)

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    sum(x, y)
```
</details>
<details>
<summary>4. Funkcja zwracająca sumę:</summary>
```python
def sum(a, b):
    return a + b

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    result = sum(x, y)
    print("The result is", result)
```
</details>
<details>
<summary>5. Funkcja konwertująca temperaturę:</summary>
```python
def convert_temperature(temp, unit):
    if unit.upper() == 'C':
        temperature = round((temp * 9/5) + 32, 1)
        print(temp, "degrees Celsius is equal to", temperature, "degrees Fahrenheit")
    elif unit.upper() == 'F':
        temperature = round((temp - 32) * 5/9, 1)
        print(temp, "degrees Fahrenheit is equal to", temperature, "degrees Celsius")
    else:
        print("Invalid unit of measurement")

if __name__ == "__main__":
    temperature = float(input())
    unit = input().strip().upper()
    convert_temperature(temperature, unit)
```
</details>
<details>
<summary>6. Funkcja sprawdzająca rok przestępny:</summary>
```python
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    year = int(input())
    if is_leap_year(year):
        print("It is a leap year")
    else:
        print("It is not a leap year")
```
</details>
<details>
<summary>7. Funkcja zwracająca największą wartość z listy:</summary>
```python
def find_max(numbers):
    return max(numbers)

if __name__ == "__main__":
    numbers = []
    for i in range(5):
        num = int(input())
        numbers.append(num)
    max_number = find_max(numbers)
    print("The largest number is:", max_number)
```
</details>
<details>
<summary>8. Funkcja rekurencyjna:</summary>
```python
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

if __name__ == "__main__":
    x = int(input())
    n = int(input())
    result = power(x, n)
    print(result)
```
</details>
<details>
<summary>9. Funkcja obliczająca silnię:</summary>
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input())
    result = factorial(n)
    print(result)
```
</details>
<details>
<summary>10. Funkcja filtrująca:</summary>
```python
# Write your function here
def test_elements(elements, test_function):
    a = []
    for i in elements:
        if test_function(i):
            a.append(i)
    return a

# Do not remove the following lines
if __name__ == '__main__':
    def test_even(value):
        return value % 2 == 0

    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    passing_elements = test_elements(elements, test_even)

    print(passing_elements)
```
</details>
</ul>
</details>

<details>
<summary>B) Listy</summary>
<ul>
<details>
<summary>1. Średnia z listy:</summary>
```python
numbers = [10, 12, 100, 125, 6]
average = sum(numbers) / len(numbers)
print(average)

# Usuwanie elementów z listy:
N = int(input())

numbers = [int(input()) for _ in range(N)]

print(numbers)

extra_number = int(input())

while extra_number in numbers:
    numbers.remove(extra_number)

print(len(numbers))
print(numbers)
```
</details>
<details>
<summary>2. Tabliczka mnożenia:</summary>
```python
N = int(input())
multiplication_table = [[(i + 1) * (j + 1) for j in range(N)] for i in range(N)]
for row in multiplication_table:
    print(row)
```
</details>
<details>
<summary>3. Nieskończona lista:</summary>
```python
tab = []
minimum = float('inf')
maximum = float('-inf')

while True:
    data = input()
    if data == "end":
        break
    else:
        data = int(data)
        tab.append(data)
        if data > maximum:
            maximum = data
        if data < minimum:
            minimum = data

minimumCounter = tab.count(minimum)
maximumCounter = tab.count(maximum)

while minimum in tab:
    tab.remove(minimum)
while maximum in tab:
    tab.remove(maximum)

while maximumCounter:
    tab.append(maximum)
    maximumCounter -= 1
while minimumCounter:
    tab.insert(0, minimum)
    minimumCounter -= 1

print(tab)
```
</details>
<details>
<summary>4. Lista punktów kontrolnych:</summary>
```python
import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))
    target_x, target_y = map(float, input().split())
    target_point = (target_x, target_y)

    distances = [(distance(point, target_point), point) for point in points]
    sorted_distances = sorted(distances)

    result = [(dist, point) for dist, point in sorted_distances]
    print(result)

if __name__ == "__main__":
    main()
```
</details>
<details>
<summary>5. Sortowanie tablicy:</summary>
```python
def main():
    numbers = list(map(int, input().split()))
    start, end = map(int, input().split())
    direction = input()

    numbers_to_display = [num for num in numbers if start <= num <= end]

    if direction == 'r':
        numbers_to_display.sort()
    elif direction == 'm':
        numbers_to_display.sort(reverse=True)

    print(*numbers_to_display)

if __name__ == "__main__":
    main()
```
</details>
</ul>
</details>


<details>
<summary>C) Klasy i obiekty</summary>
<ul>
<details>
<summary>1. MojaKlasa:</summary>
```python
class MyClass:
    def welcome(self):
        print("Welcome user")

if __name__ == '__main__':
    myObject = MyClass()
    myObject.welcome()
```
</details>
<details>
<summary>2. Prosta klasa I:</summary>
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name}: Woof!")

if __name__ == '__main__':
    my_dog = Dog("Buddy")
    my_dog.bark()
```
</details>
<details>
<summary>3. Prosta klasa II:</summary>
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

if __name__ == '__main__':
    name = input()
    age = int(input())
```
</details>
<details>
<summary>4. Klasa dla liczby binarnej:</summary>
```python
class BinaryNumber:
    def __init__(self, decimal):
        self.decimal = decimal
        self.binary = bin(decimal)[2:]  # [2:] to pominięcie '0b' na początku
    
    def show(self):
        print(self.binary)

if __name__ == '__main__':
    decimal = int(input())
    binary_number = BinaryNumber(decimal)
    binary_number.show()
```
</details>
<details>
<summary>5. Klasa Employee:</summary>
```python
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")

    def give_raise(self, amount):
        self.salary += amount

if __name__ == '__main__':
    name = input()
    employee_id = int(input())
    salary = float(input())
    raise_amount = float(input())

    employee = Employee(name, employee_id, salary)
    employee.display_info()
    employee.give_raise(raise_amount)
    employee.display_info()
```
</details>
<details>
<summary>6. Punkty na płaszczyźnie 2D i w przestrzeni 3D:</summary>
```python
class Point2D:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def dist(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = int(z)

    def dist(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** 0.5

if __name__ == "__main__":
    p1 = Point3D(1, 1, 1)
    p2 = Point3D(2, 1, 1)
    print(p1.dist(p2))
    p3 = Point2D(1, 1)
    p4 = Point2D(3, 1)
    print(p3.dist(p4))
    print(isinstance(p3, Point3D))  # False
    print(isinstance(p3, Point2D))  # True
```
</details>
<details>
<summary>7. Dziedziczenie I:</summary>
```python
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Species: {self.species}")


class Mammal(Animal):
    def __init__(self, name, age, species, num_legs):
        super().__init__(name, age, species)
        self.num_legs = num_legs

if __name__ == "__main__":
    name = input()
    age = int(input())
    species = input()
    num_legs = int(input())
    my_mammal = Mammal(name, age, species, num_legs)
    my_mammal.display_info()
```
</details>
<details>
<summary>8. Dziedziczenie II:</summary>
```python
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Species: {self.species}")


class Mammal(Animal):
    def __init__(self, name, age, species, num_legs):
        super().__init__(name, age, species)
        self.num_legs = num_legs

    def display_info(self):
        super().display_info()
        print(f"Legs: {self.num_legs}")

if __name__ == "__main__":
    name = input()
    age = int(input())
    species = input()
    num_legs = int(input())
    my_mammal = Mammal(name, age, species, num_legs)
    my_mammal.display_info()
```
</details>
<details>
<summary>9. Lista obiektów:</summary>
```python
class Book:
    def __init__(self, title, author, year_of_publication):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        found = False
        for book in self.books:
            if book.title == title:
                found = True
                print(f"{title} found!\nAuthor: {book.author}\nYear of Publication: {book.year_of_publication}")
                break
        if not found:
            print(f"{title} not found.")

if __name__ == "__main__":
    library = Library()

    book1 = Book("The Little Prince", "Antoine de Saint-Exupéry", 1943)
    book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
    book3 = Book("The Hobbit", "J.R.R. Tolkien", 1937)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    title = input()

    library.find_book(title)
```
</details>
<details>
<summary>10. Bankowość internetowa:</summary>
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def showBalance(self):
        return self.balance

if __name__ == '__main__':
    account = BankAccount()

    d1 = int(input())
    d2 = int(input())
    account.deposit(d1)
    account.deposit(d2)

    w1 = int(input())
    w2 = int(input())
    w3 = int(input())
    account.withdrawal(w1)
    account.withdrawal(w2)
    account.withdrawal(w3)

    print(account.showBalance())
```
</details>
</ul>
</details>
<details>
<summary>Kolekcje</summary>
<ul>
<details>
<summary>1. Słownik potęg:</summary>
```python
def generate_powers_of_two_dict(n):
    powers_dict = {}
    for i in range(1, n + 1):
        powers_dict[i] = 2 ** i
    return powers_dict

if __name__ == "__main__":
    n = int(input())
    powers_dict = generate_powers_of_two_dict(n)
    print(powers_dict)
```
</details>

<details>
<summary>2. Budowanie słownika:</summary>
```python
# Write your function here
def text2dict(text):
    text = text.strip().split("\n")
    dct = {}
    for elem in text:
        elem = elem.split(": ")
        dct[elem[0]] = elem[1]
    return dct

# Do not remove the following lines
if __name__ == '__main__':
    d = text2dict("""k1: w1
k2: W2
k3: w3""")
    print(d)
```
</details>

<details>
<summary>3. Unikalne słowa:</summary>
```python
words = {}
n = int(input())
while n:
    data = input().lower()
    data = ''.join(filter(lambda x: x.isalnum() or x.isspace(), data))
    data = data.split()
    for word in data:
        if words.get(word) == None:
            words[word] = 1
        else:
            words[word] += 1
    n -= 1
for key in sorted(words):
    print(key, words[key])
```
</details>

<details>
<summary>4. Lista o maksymalnej sumie elementów:</summary>
```python
def sort_numbers(numbers):
    number_dict = {'positive': [], 'negative': []}
    
    for num in numbers:
        if num >= 0:
            number_dict['positive'].append(num)
        else:
            number_dict['negative'].append(num)
    
    sum_positive = sum(number_dict['positive'])
    sum_negative = sum(abs(num) for num in number_dict['negative'])
    
    if sum_positive >= sum_negative:
        return number_dict['positive']
    else:
        return number_dict['negative']

# Test the function
if __name__ == "__main__":
    numbers = [-12, 1, 11, 5, -6]
    print(sort_numbers(numbers))
```
</details>

<details>
<summary>5. Pozycja elementu w liście:</summary>
```python
def position_of_element_in_list(lists, x):
    result = []
    for i, lst in enumerate(lists):
        for j, elem in enumerate(lst):
            if elem == x:
                result.append((i, j))
    return result

# Test the function
if __name__ == "__main__":
    n = int(input())
    x = int(input())
    lists = []
    for _ in range(n):
        lists.append(list(map(int, input().split())))
    print(position_of_element_in_list(lists, x))
```
</details>

<details>
<summary>6. Zarządzanie słownikiem:</summary>
```python
def manage_dictionary(dct, o):
    if o == 1:
        key, value = input().split()
        if key in dct:
            print("Key already in dictionary")
        else:
            dct[key] = value
    elif o == 2:
        key, value = input().split()
        if key not in dct:
            print("Can't modify non existing key")
        else:
            dct[key] = value
    elif o == 3:
        print(dct)

# Test the function
if __name__ == "__main__":
    dct = {}
    n = int(input())
    for _ in range(n):
        operation = int(input())
        manage_dictionary(dct, operation)
```
</details>
</ul>
</details>
<details>
<summary>Operacje tekstowe</summary>
<ul>
<details>
<summary>1. Warunki dotyczące linii tekstu:</summary>
```python
import sys
pat = input().strip()
text = sys.stdin.readlines()
elems = []
for line in text:
    if pat in line:
        elems.append(line.strip())
print(elems)
```
</details>

<details>
<summary>2. Formatowanie linii tekstu:</summary>
```python
n = int(input())
while n:
    print(''.join(filter(lambda x: x.isalpha() or x.isspace(), input().lower())))
    n -= 1
```
</details>

<details>
<summary>3. Formatowanie linii tekstu II:</summary>
```python
x, n = map(int, input().split())
text = ""
for _ in range(n):
    text += input().strip() + " "
formatted_text = [text[i:i+x] for i in range(0, len(text), x)]
print("\n".join(formatted_text))
```
</details>

<details>
<summary>4. Wyrażenie regularne:</summary>
```python
import re
p = re.compile(r'(?:[0-9a-fA-F][0-9a-fA-F]:?){6}')
n = int(input())
while n:
    text = input()
    for mac in re.findall(p, text):
        print(mac)
    n -= 1
```
</details>

<details>
<summary>5. Walidacja numerów kont:</summary>
```python
import re

def validate(data):
    data = data.replace(' ', '').strip()
    if len(data) != 22:
        return "NO"
    p = re.compile(r'^GB([0-9]{2})([A-Z]{4})([0-9]{14})$')
    if re.match(p, data):
        return "YES"
    return "NO"

n = int(input())

while n:
    n -= 1
    data = input()
    print(validate(data))
```
</details>

<details>
<summary>6. Szyfr Cezara:</summary>
```python
text = input()
shift = int(input())

encrypted_text = ""

for char in text:
    if char.isalpha():
        if char.islower():
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    else:
        encrypted_char = char
    encrypted_text += encrypted_char

print(encrypted_text)
```
</details>
</ul>
</details>
