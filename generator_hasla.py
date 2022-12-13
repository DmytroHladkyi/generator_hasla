import sys
import random
import string

password = []
characters_left = -1

def update_charakters_left(number_of_charakter):
    global characters_left
    if number_of_charakter < 0 or number_of_charakter > characters_left:
        print("Liczba znaków z poza przedziału 0", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_charakter
        print("Liczba znaków zostało:", characters_left)

password_length = int(input("Jak dlugie ma być hasło?"))

if password_length < 5:
    print("Hasło jest za krótkie")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letter = int(input("Ile mały litter powinno być?"))
update_charakters_left(lowercase_letter)

uppercase_letter = int(input("Ile dużych litter powinno być?"))
update_charakters_left(uppercase_letter)

special_charakters= int(input("Ile znaków specjalnych powinno być?"))
update_charakters_left(special_charakters)

gigits = int(input("Ile cyfr powinno być?"))
update_charakters_left(gigits)

if characters_left > 0:
    print("Nie wszystkie znaki zostały wykorzystane. Hasło zostanie uzupełnione malymi znakami")
    lowercase_letter += characters_left

print("Dlugość hasla:", password_length)
print("Małe litery:", lowercase_letter)
print("Duzę litery:", uppercase_letter)
print("Znaki zpecjalne:", special_charakters)
print("Cyfry:", gigits)

for _ in range(password_length):
    if lowercase_letter > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letter -= 1
    if uppercase_letter > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letter -= 1
    if special_charakters > 0:
        password.append(random.choice(string.punctuation))
        special_charakters -= 1
    if gigits > 0:
        password.append(random.choice(string.digits))
        gigits -= 1

random.shuffle(password)
print("Twoje hasło: ","".join(password))