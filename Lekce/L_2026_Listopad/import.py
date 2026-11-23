import math

print (f"PI JE: {math.pi}")
print (f"PI NENÍ : {math.pi+1 or math.pi-1}")
print (f"SINUS JE: {math.sin(math.pi/2)}")

def bezpecne_deleni(a, b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print(f"Nelze dělit nulou! {zde}")
        return None
    except Exception as e:
        print(f"Nastala neočekávaná chyba: {e}")
        return None
    finally:
        print("Dělení bylo provedeno.")
        print("Tento blok se provede vždy")
    return vysledek

print(bezpecne_deleni(10, 2))
print(bezpecne_deleni(10, 0))

