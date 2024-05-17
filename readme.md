```
    \    /\
    )  ( ')
    (  /  )
    \(__)|
    
By
Dawid Rej
```
# Kursy python Cyberskiller odpowiedzi
<details>
<summary>Podstawy programowania w Pythonie</summary>
<ol>
<details>
<summary>Podstawy pracy w środowisku Python oraz typy danych w języku Python</summary>
<ul>
<details>
<summary>1. Pierwszy program:</summary>

```python
print("my first program")
```

</details>
<details>
<summary>2. Pierwsza zmienna:</summary>

```python
data = "my first program"
print(data)
```
</details>
<details>
<summary>3. Wyświetlanie zmiennych:</summary>

```python
number = 12
pi = 3.14
date = "August 12th 2011"
condition = True
print(number)
print(pi)
print(date)
print(condition)
```
</details>
<details>
<summary>4. Wyświetlanie zmiennych II:</summary>

```python
a = 13
b = 8.78
c = "text_value"
d = True
print(a)
print(b)
print(c)
print(d)
```
</details>
<details>
<summary>5. Typy zmiennych:</summary>

```python
number_1 = 12
pi = 3.14159
date = "August 12th 2011"
condition = True
print(type(number_1))
print(type(pi))
print(type(date))
print(type(condition))
```
</details>
<details>
<summary>6. Konwersja typów:</summary>

```python
x = 1995
x = str(x)
print(type(x))
```
</details>
<details>
<summary>7. Konwersja napisu na liczby:</summary>

```python
x = "15.78"
a = float(x)
b = int(float(x))
print(a)
print(b)
```
</details>
<details>
<summary>8. Łączenie napisów:</summary>

```python
a = "Hello "
b = "world"
print(a + b)
```
</details>
<details>
<summary>9. Łączenie napisów II:</summary>

```python
text = "I was born in "
year = 1987
short_story = text + str(year) + "."
print(short_story)
```
</details>
<details>
<summary>10. Konkatenacja zmiennych:</summary>

```python
a = "My number is "
b = 15
x = a + str(b)
print(x)
```
</details>
<details>
<summary>11. Nieoczekiwana operacja mnożenia:</summary>

```python
number = "7"
print("The result of 5*" + number + " is:", 5 * int(number))
```
</details>
<details>
<summary>12. Trójkąt:</summary>

```python
print("*")
print("*" * 2)
print("*" * 3)
print("*" * 4)
```
</details>
<details>
<summary>13. Trójkąt II:</summary>

```python
for i in range(4):
    for j in range(i+1):
        print("*", end="")
    if i != 3:
        print()
```
</details>
<details>
<summary>14. Odcinek:</summary>

```python
n = 10
print("|", "-" * n, "|", sep="")
```
</details>
<details>
<summary>15. Komentowanie kodu:</summary>

```python
# AADASDASDJHASKDJHAKJSDHAKJSDHKJASHDKJASHdJASDH
#asdadsasd
a = 6
#sadadsads
b = 2
#sdadsasdadsdas
print(a % b == 0)
```
</details>
<details>
<summary>16. Test sprawdzający</summary>

## 1.Która z poniższych odpowiedzi najlepiej opisuje poprawne zasady nazywania zmiennych? 
> Nazwa powinna zaczynać się od litery i nie może być taka sama jak słowo kluczowe.
## 2.Która z poniższych odpowiedzi nie jest typem zmiennej w języku Python?
> unsigned
## 3.Każda zmienna w języku Python jest: 
> obiektem
## 4.Który z poniższych operatorów może służyć do łączenia tekstu? 
> `+`
## 5.Który z poniższych typów zmiennych służy do reprezentacji liczb całkowitych? 
> int
## 6.Która z poniższych odpowiedzi będzie wynikiem wykonania bloku instrukcji załączonego na obrazku?
> 5
## 7.Który z poniższych symboli służy do rozpoczęcia jednowierszowego komentarza w kodzie? 
> `#`
## 8.Która z poniższych funkcji służy do wypisywania tekstu na ekranie? 
> print()
## 9.Słowa kluczowe to: 
> zarezerwowane nazwy specjalne definiujące elementy składni języka Python.
## 10.Która z poniższych odpowiedzi będzie wynikiem wykonania bloku instrukcji przedstawionego na obrazku? 
> "Halo Halo Halo"



</details>
</details>
</ul>
<details>
<summary>Operator porównania, operator logiczny i komentarze</summary>
<ul>
<details>
<summary>1. Test logiczny:</summary>

```python
# Insert your code here
number = 12
test = number > 10
print(type(test))
```
</details>
<details>
<summary>2. Wyrażenie logiczne:</summary>

```python
a = 16.5
b = 16
print(a > b)
print(a < b)
print(a == b)
a = int(a)
print(a > b)
print(a < b)
print(a == b)
```
</details>
<details>
<summary>3. Testy logiczne:</summary>

```python
imie = "Jacek"
wiek = 14
klasa = "3a"
print(imie == "Jacek" and wiek < 18)
print(klasa == "3b" or imie == "Wojtek")
```
</details>
<details>
<summary>4. Przekształcenie i porównanie zmiennej liczbowej:</summary>

```python
x = 18
x += 2
print(x == 20)
x *= -1
print(x == -20)
```
</details>
<details>
<summary>5. Test parzystości:</summary>

```python
number = 23
# Insert your code here
print("Parity test: " + str(number % 2 == 0))
```
</details>
<details>
<summary>6. Test parzystości II:</summary>

```python
number = 12
# Insert your code here
print("Parity test: " + str(int(number % 2 == 0)))
```
</details>
<details>
<summary>7. Test parzystości III:</summary>

```python
number = 13
# Insert your code here
print("Liczba " + str(number) + " jest " + ("parzysta." if number % 2 == 0 else "nieparzysta."))
```
</details>
<details>
<summary>8. Test sprawdzający</summary>

## 1.Która z poniższych odpowiedzi będzie wynikiem wykonania bloku instrukcji przedstawionego na obrazku?
> 6
## 2.Jaką operacje wykonuje operator "%"? 
> Zwraca wartość reszty z dzielenia.
## 3.Który z poniższych to operator przypisania? 
> `=`
## 4.Jakie jest słowo kluczowe operatora logicznego alternatywy? 
> `or`
## 5.Do czego służy operator porównania: "<="? 
> Do sprawdzenia, czy wartość przed operatorem jest mniejsza lub równa względem wartości za operatorem.

> Do sprawdzenia, czy wartość za operatorem jest większa lub równa względem wartości przed operatorem.
## 6.Który z poniższych to operator potęgowania?
> `**`
## 7.Koniunkcja jako operator logiczny daje w wyniku prawdę (True) wtedy i tylko wtedy gdy: 
> obie wartości, które nią łączymy są typu prawda (True).
## 8.Która z poniższych odpowiedzi będzie wynikiem wykonania instrukcji przedstawionej na obrazku? 
`True`
## 9.Która z poniższych odpowiedzi będzie wynikiem wykonania bloku instrukcji przedstawionego na obrazku? 
`True`
    
</details>
</ul>
</details>
<details>
<summary>Instrukcje wejścia i wyjścia</summary>
<ul>
<details>
<summary>1. Wprowadzanie własnych danych do programu:</summary>

```python
number = input()
print(type(number))
```
</details>
<details>
<summary>2. Dodawanie dwóch liczb:</summary>

```python
# Input your code here
a = int(input())
b = int(input())
print(f"Sum of numbers {a} and {b} is {a+b}")
```
</details>
<details>
<summary>3. Pobranie informacji od użytkownika:</summary>

```python
a = input("What is your name?")
b = int(input('How old are you?'))
print(f"Your name is {a}\nYou are {b} years old")
```
</details>
<details>
<summary>4. Wynik testu logicznego:</summary>

```python
a = int(input())
b = int(input())
print(a % b == 0)
```
</details>
<details>
<summary>5. Suma wylosowanych liczb:</summary>

```python
import random
c = int(input())
d = int(input())
e = int(input())
f = int(input())
a, b = random.randint(c, d-1), random.randint(e, f-1)
print(a + b)
```
</details>
<details>
<summary>6. Pobranie danych od użytkownika i weryfikacja warunku:</summary>

```python
import random
c = int(input())
d = int(input())
b = int(input())
a = random.randint(c, d)
print(a == b)
```
</details>
<details>
<summary>7. Test sprawdzający</summary>
    
## 1.Która z poniższych metod modułu random służy do generowania liczb całkowitych? 
> `randrange`
## 2.Jakiego typu zmienną wczytujemy wykonując instrukcję pokazaną na obrazku? 
> `int`
## 3.Która z poniższych funkcji służy do pobierania danych wprowadzonych z klawiatury? 
> `input()`
## 4.celu załadowania udostępnionego modułu random posłużymy się słowem kluczowym: 
> `import`
## 5.Która z poniższych metod modułu random służy do generowania liczb rzeczywistych? 
> `random`
## 6.Jaki będzie wynik wykonania bloku instrukcji zawartych w poniższym rysunku? 
> `liczba rzeczywista z przedziału <5;6)`

</details>
</ul>
</details>
<details>
<summary>Instrukcje warunkowe</summary>
<ul>
<details>
<summary>1. Porównanie liczby:</summary>

```python
a = int(input())
print("Number is less than twenty" if a < 20 else "")
```
</details>
<details>
<summary>2. Porównanie liczby II:</summary>

```python
print("Number is greater than or equal to twenty" if int(input()) >= 20 else "Number is less than twenty")
```
</details>
<details>
<summary>3. Porównanie liczby III:</summary>

```python
a = int(input())
print("Number is greater than twenty" if a > 20 else "Number is equal to twenty" if a == 20 else "Number is less than twenty")
```
</details>
<details>
<summary>4. Test pełnoletności:</summary>

```python
a = input()
b = input()
c = int(input())
print(f"Hi {a} {b}, you are {'of legal age' if c >= 18 else 'underage'}")
```
</details>
<details>
<summary>5. Dzień tygodnia:</summary>

```python
a = int(input())
b = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
print(b.get(a))
```
</details>
<details>
<summary>6. Weryfikacja loginu:</summary>

```python
def isupperall(a):
    b = "a"
    for i in a:
        if i.isupper():
            return True
    return False


a = input()
if a == 'Admin':
    print("Login correct")
elif isupperall(a):
    print("Login incorrect")
else:
    if len(a)>5:
        print("Login correct")
    else:
        print("Login incorrect")

```
</details>
<details>
<summary>7. Test sprawdzający:</summary>
    
## 1.Jaki będzie wynik wywołania bloku instrukcji załączonego na obrazku?
> `Else`
## 2.W celu zapisania do zmiennej napisowej s wyniku wywołania na niej metody capitalize() należy skorzystać z instrukcji:
> `s = s.capitalize()`
## 3.Jaki będzie wynik wywołania bloku instrukcji załączonego na poniższym rysunku? 
> `Hello`
## 4.Jaki będzie wynik wywołania bloku instrukcji załączonego na poniższym rysunku? 
> `False`
## 5.Metoda split(separator) wymaga wywołania z podaniem argumentu oznaczającego separator. Czy to prawda, że separator może być dowolnym znakiem? 
> Prawda
## 6.Jakie słowo kluczowe należy wykorzystać, aby instrukcja if mogła wykonać inne instrukcje w przypadku, gdy warunek jest fałszywy?
> `else`
## 7.W celu wyodrębnienia bloku instrukcji warunkowej:
> poprzedzamy każdą instrukcję bloku wcięciem.
## 8.Wybierz poprawną składnię instrukcji warunkowej:
>if warunek:
## 9.Co zostanie wyświetlone po wykonaniu instrukcji zawartych na obrazku? 
> "ELSE"
## 10.W jakim celu stosujemy słowo kluczowe "elif" w waunkach if? 
> To słowo kluczowe jest zagnieżdzeniem kolejnego warunku if.
</details>

</ul>
</details>
<details>
<summary>Pętla</summary>
<ul>
<details>
<summary>1. Pierwsza pętla for:</summary>

```python
for i in range(10):
    print(i)
```
</details>
<details>
<summary>2. Własna pętla:</summary>

```python
for i in range(1, 11):
    print(i)
```
</details>
<details>
<summary>3. Trójkąt:</summary>

```python
a = int(input())
for i in range(a):
    print("*" * (i + 1))
```
</details>
<details>
<summary>4. Ładniejszy trójkąt:</summary>

```python
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```
</details>
<details>
<summary>5. Odwrotna funkcja range():</summary>

```python
n = -3
for i in range(20, 1, n):
    print(i)
```
</details>
<details>
<summary>6. Romb:</summary>

```python
n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```
</details>
<details>
<summary>7. Ciąg liczb:</summary>

```python
# Insert your code here
[print(i, end=" ") for i in range(1, 101)]
```
</details>
<details>
<summary>8. Pętla w pętli:</summary>

```python
n = 10
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print()
```
</details>
<details>
<summary>9. Pętla while:</summary>

```python
a = 0
# Insert your code here
while a != 11:
    print(a)
    a += 1
```
</details>
<details>
<summary>10. Pętla while II:</summary>

```python
a = 10
while a > 0:
    print(a)
    a = a - 1
```
</details>
<details>
<summary>11. Lista potęg:</summary>

```python
a = int(input())
for i in range(1, 11):
    print(a ** i)
```
</details>
<details>
<summary>12. Pętla while z warunkiem opuszczenia:</summary>

```python
condition = True
# Insert your code here
a = ""
while True:
    a = input()
    if a == "end":
        break
    else:
        print(a)
```
</details>
<details>
<summary>13. Lista dzielników:</summary>

```python
a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        print(i)
```
</details>
<details>
<summary>14. Alfabet:</summary>

```python
print("a A b B c C d D e E f F g G h H i I j J k K l L m M n N o O p P q Q r R s S t T u U v V w W x X y Y z Z")
```
</details>
<details>
<summary>15. Alfabet ze skokiem:</summary>

```python
a = "abcdefghijklmnopqrstuvwxyz"
n = int(input())
for i in range(0, len(a), n):
    print(a[i], a[i].upper(), end=" ")
```
</details>
<details>
<summary>16. Nieskończone wczytywanie:</summary>

```python
while True:
    num = input()
    if num == 'end':
        break
    num = int(num)
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
```
</details>
<details>
<summary>17. Lista słów i długości:</summary>

```python
text = input()
word_length_tuples = [(word, len(word)) for word in text.split()]
print(word_length_tuples)
```
</details>
<details>
<summary>18. Ciąg Fibonacciego:</summary>

```python
def fibonacci(n):
    fib_sequence = [0, 1]
    [fib_sequence.append(fib_sequence[-2] + fib_sequence[-1]) for _ in range(2, n)]
    return fib_sequence[:n]
n = int(input())
if n < 0:
    print("Integer must be non-negative.")
else:
    fib_list = fibonacci(n)
print(fib_list)
```
</details>
<details>
<summary>19. Konwersja liczby dziesiętnej na binarną:</summary>

```python
decimal_number = int(input())
binary_representation = bin(decimal_number)[2:]
binary_digits = [int(bit) for bit in binary_representation]
for bit in reversed(binary_digits):
    print(bit)
```
</details>
<details>
<summary>19. Test sprawdzający:</summary>
    
## 1.Oceń prawdziwość zdania: Pętla for pozwala na określenie liczby powtórzeń.
> Prawda
## 2.Które z poniższych słów kluczowych pozwala na przerwanie pętli?
> `break`
## 3.Która z poniższych instrukcji pozwala na powtarzanie wykonywanych czynności w przypadku, gdy nie znamy liczby powtórzeń?
> while
## 4.Jaki będzie wynik wywołania bloku instrukcji z załączonego obrazka? 
> `0 1 2 3 4 5`
## 5.Czym jest iteracja? 
> Iteracja to czynność powtarzania tej samej instrukcji w pętli.
## 6.Oceń prawdziwość zdania: Pętla while nie może przyjmować w warunku zmiennej typu str. 
> Fałsz
## 7.Oceń prawdziwość zdania: Gdy znamy liczbę obrotów pętli możemy zamiennie korzystać z obu rodzajów pętli: for i while.
> Prawda
## 8.Jaki będzie wynik wywołania bloku instrukcji z załączonego obrazka?
> `4 5 6 7 8`
## 9.Która z odpowiedzi poprawnie opisuje działanie bloku instrukcji zawartego na obrazku? 
> Pętla while jest pętlą nieskończoną.
</details>
</ul>
</details>

</ol>
</details>

<details>
<summary>Zaawansowane struktury w Pythonie</summary>
<ol>
<details>
<summary>Definiowanie funkcji</summary>

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
<details>
<summary>11. Test sprawdzający:</summary>
    
## Jakiego typu będzie zmienna "wynik_metody" po wykonaniu bloku instrukcji z załączonego obrazka?
> None
## Co zostanie wyświetlone na ekranie po wykonaniu operacji przedstawionej na obrazku?
> "2+3"
## Jaki będzie wynik wywołania funkcji załączonej na obrazku? 
> None
## W jakim celu posługujemy się słowem kluczowym "def" w języku Python?
> Służy do zadeklarowania funkcji.
## Jaki będzie wynik wykonania kodu przedstawionego na rysunku? 
> 1
## Ile razy wykona się funkcja przedstawiona na obrazku? 
> 5
## Jaki będzie wynik wywołania funkcji załączonej na obrazku? 
> 24
</details>
</ul>
</details>

<details>
<summary>Listy</summary>

<ul>
<details>
<summary>1. Średnia z listy:</summary>

```python
numbers = [10, 12, 100, 125, 6]
average = sum(numbers) / len(numbers)
print(average)

```
</details>

<details>
    
<summary>Usuwanie elemtnów z listy</summary>
    
```python    
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
<details>
<summary>7. Test sprawdzający</summary>

## Która z poniżej wymienionych metod pozwala na usunięcie elementu z listy? 
> remove
## Oceń prawdziwość zdania: Dodając do pustej listy elementy będące listami jednowymiarowymi otrzymamy listę dwuwymiarową. 
> Prawda
## Która z poniżej wymienionych metod pozwala na dodanie elementu na koniec listy? 
> append
## Która z poniższych odpowiedzi przedstawia sposób zadeklarowania pustej listy o nazwie example_list? 
> example_list = []
## Mając listę, która zawiera 5 elementów, pod jakim indeksem znajdzie się pierwszy element listy? 
> 0
## Jaki będzie wynik uruchomienia bloku kodu z załączonego obrazka? 
> `[0, [1, 1], 2, [3, 1]]`

</details>
</ul>
</details>
<details>
<summary>Klasy i obiekty</summary>
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
<details>
<summary>11. Test sprawdzający</summary>

## Z poniższych odpowiedzi wybierz poprawną, która uzupełnia zdanie: Każdy obiekt tworzony na podstawie klasy to jej ... .
> instancja
## Podczas deklarowania metody w klasie zazwyczaj pierwszym argumentem tej metody jest? 
> self
## Z poniższych odpowiedzi wybierz definicję klasy. 
> Klasa jest szablonem na podstawie którego tworzone są obiekty.
## Odpowiednikiem funkcji dla klas/obiektów jest:
> metoda
## W jaki sposób oznaczamy klasę bazową? 
> Podajemy jej nazwę w nawiasie w nagłówku klasy potomnej.
## Oceń prawdziwość zdania: Klasa bazowa to klasa, która odziedziczyła atrybuty i metody z klasy potomnej. 
> Fałsz
## Metoda __init__ w klasie pełni rolę: 
> konstruktora


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
<details>
<summary>7.Test sprawdzający</summary>
    
## Oceń prawdziwość zdania. Zbiór (set) pozwala na zmianę wartości jego elementów.
> Fałsz
## Oceń prawdziwość zdania. Lista pozwala na przechowywanie elementów o dowolnym typie.
> Prawda
## Oceń prawdziwość zdania. Krotka (tuple) inicjalizowana jest tylko i wyłącznie za pomocą nawiasów okrągłych. 
> Która z poniższych odpowiedzi jest fałszywa?
## Składnia "for element in list" pozwala na iterowanie przez elementy listy
> Prawda
## Funkcja len() pozwala na sprawdzenie liczby elementów w liście
> Prawda
## Operator + pozwala na konkatenację list
> Prawda
## Oceń prawdziwość zdania. Para klucz i wartość przechowywana w słowniku musi być tego samego typu.
> Fałsz
## Która z poniższych odpowiedzi pozwoli na dodanie elementu do listy?
> list.append(el)
## Oceń prawdziwość zdania. Krotka (tuple) to struktura przechowująca tylko dwie zmienne.
> Fałsz
## Oceń prawdziwość zdania. Lista to uporządkowana kolekcja pozwalająca na przechowywanie określonej liczby elementów.
> Fałsz
## Oceń prawdziwość zdania. Słownik (dictionary) to nieuporządkowany zbiór elementów, dostęp do wartości elementów możliwy jest za pomocą kluczy.
> Prawda
## Oceń prawdziwość zdania. Zbiór (set) to uporządkowany zbiór danych. 
> Fałsz
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

<details>
<summary>7. Test sprawdzający</summary>
    
## Która z poniższych odpowiedzi przedstawia operację wczytania wszystkich wierszy z wejścia, zapisywanych do listy? 
> sys.stdin.readlines()
## Oceń prawdziwość zdania. Metoda islower() służy do zamiany napisu na napis skaładający się tylko i wyłącznie z małych liter.
> Fałsz
## Który z poniższych odpowiedzi posłuży do dopasowania dowolnego ciągu znaków w wyrażeniach regularnych?
> Fałsz
## Która z poniższych funkcji modułu re służy do zwrócenia obiektu reprezentującego wyrażenie regularne? 
> re.compile()
## Oceń prawdziwość zdania. Moduł re zawiera funkcje obsługujące wyrażenia regularne
> Prawda
## Który z poniższych znaków służy do dopasowania wyrażenia zaczynającego się od wskazanej po znaku litery? 
> "^"
## Która z poniższych metod klasy str służy do usuwania wszelkich białych znaków? 
> replace()
## Która z poniższych metod służy do stworzenia napisu, który składa się tylko i wyłącznie z wielkich liter?
> upper()
## Oceń prawdziwość zdania. Metoda isspace() zwraca wartość True, jeżeli wszystkie znaki napisu są znakami białymi.
> Prawda

</ul>
</details>

</ol>
</details>

<details>
<summary>Zaawansowane struktury w Pythonie - dodatkowa praktyka </summary>
<ol>
<details>

<summary>Definiowanie funkcji</summary>  
<uL>
<details>
<summary>1. Pożegnanie:</summary>

```python
# Define your function here
def goodbye(imie):
    print(f"Goodbye, {imie}! It was nice to see you.")

if __name__ == "__main__":
    goodbye(input())
```
</details>

<details>
<summary>2. Pierwiastek kwadratowy:</summary>

```python
import math

def square_root(n):
    if n == "0":
        print(1)
    print(round(math.sqrt(2), int(n)))

if __name__ == "__main__":
    square_root(input())
```
</details>

<details>
<summary>3. Wyprzedaż:</summary>

```python
def discount(price, percent):
    discounted_price = price * (1 - percent / 100)
    return round(discounted_price, 2)

if __name__ == "__main__":
    price = float(input())
    percent = int(input())
    result = discount(price, percent)
    print(result)
```
</details>

<details>
<summary>4. Ułamki zwykłe:</summary>

```python
def fraction_decimal(n, k):
    result = n / k
    return round(result, 2)

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    result = fraction_decimal(n, k)
    print(result)
```
</details>
<details>
<summary>5. Ułamki zwykłe II:</summary>

```python
def fraction_decimal(n, k):
    result = n / k
    return round(result, 2)

def add_fractions(n1, k1, n2, k2):
    numerator = n1 * k2 + n2 * k1
    denominator = k1 * k2
    return fraction_decimal(numerator, denominator)

if __name__ == "__main__":
    n1 = int(input())
    k1 = int(input())
    n2 = int(input())
    k2 = int(input())
    result = add_fractions(n1, k1, n2, k2)
    print(result)
```
</details>
<details>
<summary>6. Obwód wielokąta:</summary>

```python
# Define your function here
def polygon_perimeter(sides_lengths):
    perimeter = sum(sides_lengths)
    return perimeter

if __name__ == "__main__":
    perimeter = polygon_perimeter([3, 4, 5, 6])
    print(perimeter)
```
</details>
<details>
<summary>7. Dni tygodnia:</summary>

```python
def day_of_week(day_name, n):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_index = days_of_week.index(day_name.capitalize())
    future_day_index = (day_index + n) % 7
    return days_of_week[future_day_index]

if __name__ == "__main__":
    day_name = input().capitalize()
    n = int(input())
    result = day_of_week(day_name, n)
    print(result)
```
</details>
<details>
<summary>8. NWD:</summary>

```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    result = gcd(a, b)
    print(result)
```
</details>
</ul>
</details>
<details>
    <summary>Listy</summary>
<ul>

<details>





<summary>1. Suma z tablicy:</summary>

```python
'''Define numbers list here'''
numbers = (3, 7, 11, 15, 19, 23)
if __name__ == "__main__":
    suma = sum(numbers)
    print(suma)
```
</details>
<details>
<summary>2. Usuwanie elementów:</summary>

```python
if __name__ == "__main__":
    '''Insert your code here'''
    a = input()
    b = input()
    c = input()
    d = list(a + b)
    print(d)
    print(len([i for i in d if i != c]))
    print([i for i in d if i != c])
```
</details>
<details>
<summary>3. Dwie listy:</summary>

```python
'''Define and build your lists here'''
n = int(input())
positive = []
negative = []
for i in range(n):
    if (a := int(input())) < 0:
        negative.append(a)
    else:
        positive.append(a)

if __name__ == "__main__":
    '''Print your lists here'''
    print(positive)
    print(negative)
```
</details>
<details>
<summary>4. Macierz:</summary>

```python
'''Define and fill in the matrix variable here'''
a = int(input())
b = int(input())
matrix = [[0] * a for _ in range(a)]
# print(matrix)
for i in range(a):
    for j in range(a):
        matrix[i][j] = b
        b += 1

if __name__ == "__main__":
    '''Print elements of the matrix here'''
    for i in matrix:
        print(*i)
```
</details>
</ul>
</details>
<details>
    <summary>Klasy i obiekty</summary>
    <ul>
<details>
<summary>1. Klasa Townspeople:</summary>

```python
class Townspeople:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

if __name__ == "__main__":
    person = Townspeople("John", 30)
    person.greet()
```
</details>

<details>
<summary>2. Klasa Car:</summary>

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        print(f"This car is a {self.brand} {self.model} from {self.year}.")

if __name__ == "__main__":
    brand = input()
    model = input()
    year = int(input())
    car = Car(brand, model, year)
    car.description()
```
</details>
<details>
<summary>3. Klasa Rectangle:</summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    print("Area:", rectangle.calculate_area())
    print("Perimeter:", rectangle.calculate_perimeter())
```
</details>
<details>
<summary>4. Klasa Product:</summary>

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def add_stock(self, amount):
        self.quantity += amount

if __name__ == "__main__":
    product = Product("Chocolate", 2.99, 100)
    product.add_stock(50)
    product.display_info()
```
</details>
<details>
<summary>5. Klasa Vehicle:</summary>

```python
class Vehicle:
    def __init__(self, brand, model, year, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Engine:", self.engine)

class Car(Vehicle):
    def __init__(self, brand, model, year, engine, num_doors):
        super().__init__(brand, model, year, engine)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print("Number of doors:", self.num_doors)

if __name__ == "__main__":
    car = Car("Ford", "Mustang", 2020, "V8", 2)
    car.display_info()
```
</details>
<details>
<summary>6. Klasa Shape:</summary>

```python
class Shape:
    def __init__(self, color):
        self.color = color
        self.area = None

    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        self.calculate_area()
    def calculate_area(self):
        self.area = round(3.14 * self.radius ** 2, 2)
    def display_info(self):
        print("Color:", self.color)
        print("Radius:", self.radius)
        print("Area:", self.area)
if __name__ == "__main__":
    circle = Circle("blue", 5)
    circle.display_info()
```
</details>
<details>
<summary>7. Klasa dla liczby zespolonej:</summary>

```python
import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imag_diff = self.imag - other.imag
        return ComplexNumber(real_diff, imag_diff)

    def __mul__(self, other):
        real_product = self.real * other.real - self.imag * other.imag
        imag_product = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_product, imag_product)

    def __lt__(self, other):
        return math.sqrt(self.real ** 2 + self.imag ** 2) < math.sqrt(other.real ** 2 + other.imag ** 2)

    def __gt__(self, other):
        return math.sqrt(self.real ** 2 + self.imag ** 2) > math.sqrt(other.real ** 2 + other.imag ** 2)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        return f"{self.real}{'+' if self.imag >= 0 else ''}{self.imag}i"
if __name__ == "__main__":
    num1 = ComplexNumber(int(input()), int(input()))
    num2 = ComplexNumber(int(input()), int(input()))
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 < num2)
```
</details>
<details>
<summary>8. Baza danych książek:</summary>

```python
class Book:
    def __init__(self, book_id, isbn, title, author):
        self.book_id = book_id
        self.isbn = isbn
        self.title = title
        self.author = author

    def check(self, pattern):
        return pattern in [self.isbn, self.title, self.author]

    def modify(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author

    def get_id(self):
        return self.book_id

    def __str__(self):
        return f"{self.book_id} {self.isbn} {self.title} {self.author}"


class Library:
    def __init__(self):
        self.current_id = 0
        self.books = []

    def add(self, isbn, title, author):
        book = Book(self.current_id, isbn, title, author)
        self.books.append(book)
        self.current_id += 1

    def modify(self, id, isbn, title, author):
        for book in self.books:
            if book.get_id() == id:
                book.modify(isbn, title, author)
                break

    def delete(self, id):
        self.books = [book for book in self.books if book.get_id() != id]

    def find(self, pattern):
        found_books = [book for book in self.books if book.check(pattern)]
        for book in found_books:
            print(book)

# Test
if __name__ == '__main__':
    library = Library()

    library.add("83-7316-152-X", "TheOldManandTheSea", "Hemingway")
    library.add("978-83-800-8211-3", "HarryPotterAndThePhilosophersStone", "Rowling")

    library.find("Rowling")
    library.find("Hemingway")

    library.modify(1, "978-83-800-8211-3", "HarryPotterAndThePhilosophersStone", "Rowling")
    library.delete(0)

    library.find("Rowling")
    library.find("Hemingway")

    print(isinstance(library.books[0], Book)) # True

```
</details>
<details>
<summary>9. Bankowość internetowa z limitem:</summary>

```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def showBalance(self):
        return self.balance

class BankAccountWithLimit(BankAccount):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def withdraw(self, amount):
        if self.balance - amount < self.limit:
            print("Insufficient funds")
        else:
            super().withdraw(amount)


if __name__ == '__main__':
    limit = int(input())
    account = BankAccountWithLimit(limit)

    d1 = int(input())
    d2 = int(input())
    account.deposit(d1)
    account.deposit(d2)

    w1 = int(input())
    w2 = int(input())
    w3 = int(input())
    account.withdraw(w1)
    account.withdraw(w2)
    account.withdraw(w3)

    print(account.showBalance())
    print(isinstance(account, BankAccount))
```
</details>
</ul>
</details>
<details>
    <summary>Kolekcje</summary>
    <ul>

<details>
<summary>1. Słownik alfabetyczny:</summary>

```python
# Write your code here
n = int(input())
a = {}
i = 97
j = 1
for x in range(n):
    if i > 122:
        a[j] = j
    else:
        a[chr(i)] = j
    i += 1
    j += 1
print(a)
```
</details>
<details>
<summary>2. Funkcja słownikowa:</summary>

```python
def remove_dict_entry(slownik, klucz):
    if klucz in slownik:
        wartosc = slownik.pop(klucz)
        return wartosc
    else:
        return -1

if __name__ == "__main__":
    my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
    klucz = input()
    wynik = remove_dict_entry(my_dict, klucz)
    if wynik == -1:
        print("Key doesn't exist")
    else:
        print(wynik)
        print(len(my_dict))
        print(my_dict)
```
</details>
<details>
<summary>3. Odległość dwóch punktów - krotki:</summary>

```python
# Implement getting values into variables here
import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
# Create tuples here
pointA = (a, b)
pointB = (c, d)

if __name__ == "__main__":
    '''Insert your code with calculations here'''
    odl = round(math.sqrt((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2), 2)
    print(odl)
```
</details>
<details>
<summary>4. Lista krotek:</summary>

```python
# Define your function here (if you use function)
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = []
    for _ in range(10):
        num = int(input().strip())
        prime = is_prime(num)
        numbers.append((num, prime))
    for num, prime in numbers:
        if not prime:
            print(num, prime)
```
</details>
</ul>
</details>

<details>
    <summary>Operacje Tekstowe:</summary>
    <ul>
<details>
<summary>1. Samogłoski:</summary>

```python
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    modified_text = ""
    for char in text:
        if char not in vowels:
            modified_text += char
    return modified_text

if __name__ == "__main__":
    text = input().strip()
    modified_text = remove_vowels(text)
    print(modified_text)
```
</details>
<details>
<summary>2. Poprawne zdania:</summary>

```python
def capitalize_first_letter(line):
    words = line.split()
    modified_line = ""
    for i, word in enumerate(words):
        if i == 0:
            modified_line += word.capitalize()
        else:
            modified_line += word.lower()
        if i != len(words) - 1:
            modified_line += " "
    if not modified_line.endswith("."):
        modified_line += "."
    return modified_line

if __name__ == "__main__":
    n = int(input().strip())
    lines = []
    for _ in range(n):
        line = input().strip()
        modified_line = capitalize_first_letter(line)
        lines.append(modified_line)

    for line in reversed(lines):
        print(line)

```
</details>
<details>
<summary>3. Podział tekstu:</summary>

```python
def split_text(text, n):
    fragments = [text[i:i + n] for i in range(0, len(text), n)]
    fragments.sort()
    return fragments

if __name__ == "__main__":
    text = input().strip()
    n = int(input().strip())
    fragments = split_text(text, n)
    for fragment in fragments:
        print(fragment)
```
</details>
</ul>
</details>

</details>
</ol>
</details>
