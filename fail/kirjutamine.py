nimi = input("Palun sisesta oma nimi: ")
vanus = input("vanus: ")
aadress = input("aadress: ")

fail = open("kirjutatud.txt", "w")
fail.write(nimi + "\n")
fail.write(vanus + "\n")
fail.write(aadress + "\n")
fail.close()