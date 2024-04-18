<details>
  <summary>Podstawy pracy w środowisku Python oraz typy danych w języku Python</summary>
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

</details>
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
    </ul>
  </details>
  