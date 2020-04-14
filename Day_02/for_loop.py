age={"Padma":23,"Pasindu":20,"Sunanada":24}

for name in age:
    print(name, age[name])

    # Padma    23
    # Pasindu    20
    # Sunanada    24


for name in sorted(age.keys()):
    print(name, age[name])

    # Padma    23
    # Pasindu    20
    # Sunanada    24


for name in sorted(age.keys(), reverse= True):
    print(name, age[name])

    # Sunanada    24
    # Pasindu    20
    # Padma    23


for name in sorted(age.values()):
    print(name )

    # 20
    # 23
    # 24

#Consider bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}.
# the code will print a greeting only to friendly bears?
# Your code should work even if more bears are added to the dictionary.
bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
    if bears[bear]== 'friendly':
        print("Hello, "+bear+" bear!")
else:
    print("odd")


