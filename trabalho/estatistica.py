from math import sqrt

a = [
13.3536,
13.9252,
15.9470,
13.7164,
13.7072,
13.0416,
14.4612,
13.2288,
12.5424,
13.4784,
12.2460,
13.4238,
12.6828,
12.9636,
16.0230,
13.4250,
14.7734,
13.4450,
13.4432,
14.1656



]
b = [
9.2508,
8.8512,
9.3212,
9.2196,
8.6580,
9.5004,
9.1416,
8.4552,
8.2212,
7.9716,
9.0168,
9.9996,
8.9388,
9.0168,
9.1728,
8.9086,
10.0564,
8.7868,
8.7054,
9.9668





]

valor = [12.71, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228, 2.201, 2.179, 2.160, 2.145,2.131, 2.120, 2.110, 2.101, 2.093, 2.086, 2.080, 2.074,2.069, 2.064, 2.060, 2.056,2.052, 2.048, 2.045, 2.042]

mediaA = 0
mediaB = 0

for elemento in a:
    mediaA += elemento

mediaA = mediaA/len(a)

for elemento in b:
    mediaB += elemento

mediaB = mediaB/len(b)

print("Media A", mediaA )
print("Media B", mediaB )

desvioPadraoA = 0

somatorioA = 0

for elemento in a:
    somatorioA += (elemento-mediaA)**2

somatorioA = (somatorioA)/(len(a)-1)
desvioPadraoA = sqrt(somatorioA)

desvioPadraoB = 0

somatorioB = 0

for elemento in b:
    somatorioB += (elemento-mediaB)**2


somatorioB = (somatorioB)/(len(b)-1)
desvioPadraoB = sqrt(somatorioB)


print("Desvio Padrao A" , desvioPadraoA)
print("Desvio Padrao B" , desvioPadraoB)

diferencaMedias = mediaA-mediaB

desvioPadraoDasDiferencas = sqrt((((desvioPadraoA)**2)/len(a)) + (((desvioPadraoB)**2)/len(b)))
sA = desvioPadraoA**4
sB = desvioPadraoB**4
nA = len(a)
nB =len(b)

print("Desvio Padrao das Diferencas", desvioPadraoDasDiferencas)
grausDeLiberdade = ((desvioPadraoDasDiferencas**4)/((1/(nA +1))*(sA/(nA**2)) +(1/(nB +1))*(sB/(nB**2)))) -2

print("Graus de Liberdade:", grausDeLiberdade)
try:
    inter = valor[round(grausDeLiberdade) -1]
except Exception:
    inter = float(input("Qual o valor mesmo?"))

print("T =" , inter)
print("(",(mediaA-mediaB) - inter*desvioPadraoDasDiferencas, " : ", (mediaA-mediaB) + inter*desvioPadraoDasDiferencas, ")")
