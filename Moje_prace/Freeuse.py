#SEZNAM PODEZŘELÝCH OSOB
my_list = ["Alfonz", "Bětka", "Cecil", "Dominik", "Eva", "Farář Bob", "Gil", "Hana", "Ivan", "Jan"]
print(f"Seznam: {my_list}")

mají_alibi = ["Alfonz", "Cecil", "Eva", "Hana", "Jan"]
nemají_alibi = ["Bětka", "Dominik", "Gil", "Ivan", "Farář Bob"]
mají_motiv = ["Farář Bob", "Alfonz", "Bětka", "Ivan"]
nemají_motiv = ["Cecil", "Dominik", "Eva", "Gil", "Hana", "Jan"]
mají_zbraň = ["Eva", "Farář Bob", "Alfonz", "Jan"]
nemají_zbraň = ["Bětka", "Cecil", "Dominik", "Gil", "Hana", "Ivan", "Jan"]
mají_příležitost = ["Bětka", "Cecil", "Dominik", "Eva", "Farář Bob", "Gil"]
nemají_příležitost = ["Alfonz", "Hana", "Ivan",]


for jméno in my_list:
    body = sum((
        jméno in nemají_alibi,
        jméno in mají_motiv,
        jméno in mají_zbraň,
        jméno in mají_příležitost,
    ))

    if body == 4:
        kategorie = "Hlavní podezřelý"
    elif body == 3:
        kategorie = "Důležitý podezřelý"
    elif body == 2 or (body == 1 and (jméno in mají_zbraň or jméno in mají_motiv)):
        kategorie = "Podezřelý"
    else:
        kategorie = "Není podezřelý"

    print(f"{jméno}: {body} bodů — {kategorie}")
