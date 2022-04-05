biblioteca={
    "Preda": "Morometii",
    "Preda": "Delirul",
    "Eminescu": "Luceafarul",
    "Creanga": "Povesti"
}
nume=str(input("Introduce numele autorului: "))
for i in biblioteca.items():
    if(biblioteca.has_key(nume)):
        print("Cartea este " + biblioteca.get(nume))