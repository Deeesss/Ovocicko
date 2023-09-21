zelenina = ["kapusta", "uhorka", "paradajka", "paprika", "redkvička", "mrkva", "brokolica"]
ovoce = ["jablko", "hruška", "pomaranč", "jahoda", "banán", "kiwi", "malina"]

input_count = 0
odpoved = "ano"

while True:
    if odpoved == "ano":
        ovocicko = input("Zadaj názov lubovolného ovocia alebo zeleniny: ")
        input_count += 1
        if ovocicko in zelenina:
            zoznam = zelenina.index(ovocicko)
            print(f"Zadal si zeleninu")
        elif ovocicko in ovoce:
            zoznam = ovoce.index(ovocicko)
            print(f"Zadal si ovocie")
        else:
            print("Tvoje slovo nemám v zoznamu")
    else:
        print(f"Zadal si", input_count, "slov", sep=" ")
        break

    odpoved = input("Prajše si zadať ďalšie slovo? (ano/ne) ")
