zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev", "mrkev", "brokolice"]
ovoce = ["jablko", "hruška", "pomeranč", "jahoda", "banán", "kiwi", "malina"]

input_count = 0
odpoved = "ano"

while True:
    if odpoved == "ano":
        ovocicko = input("Zadej název libovolného ovoce nebo zeleniny: ")
        input_count += 1
        if ovocicko in zelenina:
            zoznam = zelenina.index(ovocicko)
            print(f"Zadal jsi zeleninu")
        elif ovocicko in ovoce:
            zoznam = ovoce.index(ovocicko)
            print(f"Zadal jsi ovoce")
        else:
            print("Tvoje slovo nemám v seznamu")
    else:
        print(f"Zadal jsi", input_count, "slov", sep=" ")
        break

    odpoved = input("Přeješ si zadat další slovo? (ano/ne) ")