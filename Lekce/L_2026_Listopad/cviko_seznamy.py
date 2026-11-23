import math
# proměnné a řetězce
jmeno = "Petr"
vek = 25
print(f"Ahoj, jmenuji se {jmeno} a je mi {vek} let.")

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
numbers.sort()
print(f"Seřazený seznam: {numbers}")
print(f"První prvek seznamu: {numbers[0]}")
print(f"Poslední prvek seznamu: {numbers[-1]}")

#Slovníky a množiny

student = {}
student ["vek"] = 15
student ["jmeno"] = "Petr"
student ["predmety"] = ["Matematika", "Fyzika", "Chemie"]
print ("Student: ", student)

data = [3,3,3,4,5,6,7,8,9,9,9,10]
unique_data = set(data)
print(f"Unikátní hodnoty: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:
        print(f"{i} je dělitelné 3")
    elif i % 5 == 0:
        print(f"{i} je dělitelné 5")
    else:
        print(f"{i} není dělitelné 3 ani 5")

def vypocet_obvodu_obdelniku(delka, sirka):
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print(f"Obvod obdélníku s délkou {delka} a šířkou {sirka} je: {vypocet_obvodu_obdelniku(delka, sirka)}")

def vypocet_obvodu_telesa(delka, sirka=None):
    if sirka is None:
        sirka = delka
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print(f"Obvod tělesa s délkou {delka} a šířkou {sirka} je: {vypocet_obvodu_telesa(delka, sirka)}")


#odmocnina
odmocnina = math.sqrt(256)
print(f"Odmocnina z 256 je: {odmocnina}")