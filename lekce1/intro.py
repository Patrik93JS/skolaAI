

def sum(a,b):
    s = a + b
    return s

print(sum(5,7))

jmeno = "Zbynek"
prijmeni = "Hafik"
iq = 123

print("Obcan", jmeno, prijmeni, "Urcite nema IQ", iq)
print("Jmeno je dlouhe", len(jmeno), "znaku")

a = "63"
b = int(a)
print(type(b))

a = 63
b = str(a)
print(type(b),b)

print(jmeno[0] + "bude tu jen", jmeno[3:5])

print(jmeno * 2)

def obsah(a,b):
    s = a * b
    return s

print(obsah(11,20))


def haf(a=1, b=2):
    s = a * b
    return s

print(haf(11,23))

a = 10

def f():
    a = 30
    return a

print(a)

a = [1,2,3]

def g(a):
    a.append(5)
    return a

g(a)
print(a)

class Osoba:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
    def tisk(self):
        print(self.jmeno, self.prijmeni)

stopar = Osoba("Arthur", "Dent")
stopar.tisk()

# seznam
prvocisla = [2,3,5,7,11,13]
print(prvocisla)
prvocisla.append(19)
print(prvocisla)

bodxyz = (100, 120, 140)
jinybodxyz = 101, 111, 121

print(bodxyz)
print(jinybodxyz)
print(bodxyz[1])


# slovnik
byty = {"petr": 2, "jana": 5}
print(byty["jana"])

# mnoziny
s = set()
nakup = {"jabko", "hruska", "pomeranc"}
print(nakup)

nakup.add("tahini")
print(nakup)
nakup.remove("pomeranc")
print(nakup)

print("hruska" in nakup)

a = set("12345")
b = set('2357')

# prunik
print(a & b)
# sjednoceni
print(a | b)
# rozdil
print(a - b)
# xor
print(a ^ b)