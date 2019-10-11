import csv
import matplotlib.pyplot as plt
import math## script comparacao dos dados do mesmo sensor em leituras diferentes

##localizacao do arquivo com os dados do arquivo1
f2 = open('/home/wesley/Desktop/testesLancando/teste1/05_59_29_vehicle_air_data_0.csv', 'r' )

##localizacao do arquivo com os dados do arquivo2
#f = open('/home/wesley/Desktop/pixCSVTESTE1/teste12/04_43_42_sensor_combined_0.csv', 'r' )

##vetores da leitura 1
temp1 = []
accelZ = []## vetores da leitura 2

fim = 0

altura = []

leitor2 = csv.reader(f2)
#leitor = csv.reader(f)

cont = 0## contadores pra saltar linhas com texto

alturaRelativa = 0

for linha in leitor2:
	if cont == 0:
		cont = cont + 1
	else :
		if cont == 1:
			alturaRelativa = float(linha[3])
			temp1.append(cont - 1)
			altura.append(float(linha[3]))
			cont = cont + 1
		else :
			temp1.append(cont - 1)
			altura.append(float(linha[3]))
			cont = cont + 1

#fim = cont
#cont = 0

#for linha in leitor:
#	if cont == 0 :
#		cont = cont + 1
#	else :
#		if fim > cont:
#			accelZ.append(float(linha[8]))
#			cont = cont + 1
#		else :
#			cont = cont + 1
		
f2.close()
#f.close()

plt.subplot(2, 1, 1)
plt.plot(temp1, altura)
#plt.plot(temp1, accelZ)

plt.title('altura x tempo ')
plt.ylabel('altura/aceleracao')
plt.xlabel('time ')

plt.show()
