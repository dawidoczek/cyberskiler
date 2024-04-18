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
```
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
    </ul>
</details>
  
