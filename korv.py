import math

print("---------------------------")
print(".: KORVKOLLEN 1.0.2 :.")
print(".:  Nackademin 2023 :.")
print("---------------------------")
print("Hur många elever vill ha... ")

_2_Korv = int(input("2 vanliga korvar     > "))
_3_Korv = int(input("3 vanliga korvar     > "))
_2_Vego = int(input("2 veganska korvar    > "))
_3_Vego = int(input("3 veganska korvar    > "))

korvPack = math.ceil((2 * _2_Korv + 3 * _3_Korv) / 8)
vegoPack = math.ceil((2 * _2_Vego + 3 * _3_Vego) / 4)
drick = _2_Korv + _3_Korv + _2_Vego + _3_Vego

pris = float(20.95 * korvPack + 34.95 * vegoPack + 13.95 * drick)

print("---------------------------")
print("-       Inköpslista       -")
print("---------------------------")
print("| Vanlig korv:  ", korvPack, "förpackningar")
print("| Vegansk korv: ", vegoPack, "förpackningar")
print("| Dryck:        ", drick, "drick")

print("---------------------------")
print("| ", round(pris, 1), "SEK")
print("---------------------------")