import csv
import matplotlib.pyplot as plt
import math## script comparacao dos dados do mesmo sensor em leituras diferentes

##localizacao do arquivo com os dados do arquivo1
f2 = open('/home/wesley/Desktop/testesLancando/teste2/desc4/05_59_57_vehicle_air_data_0.csv','r')

##localizacao do arquivo com os dados do arquivo2
#f = open('/home/wesley/Desktop/pixCSVTESTE1/teste12/04_43_42_sensor_combined_0.csv', 'r' )

##vetores da leitura 1
temp1 = []
accelZ = []
accelX = []
accelY = []

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
			alturaRelativa = float(linha[1])
			temp1.append(cont - 1)
			altura.append(float(linha[1]))
			cont = cont + 1
		else :
			temp1.append(cont)
			altura.append(float(linha[1]))
			cont = cont + 1


XchapeuMaisUmDadoT = altura[0]
# erromeaBarometer = 5000 
R = 5
XchapeuT = altura[0]
# estimator pk = 1000; Q = 0.01; R = 5  for altimeter; 
pk = 1000	
		
Q = 0.00650104
alturaK = []
velzk = []
alturaK.append(altura[0])
i = 1
a1 = altura[0]
a2 = 0
a3 = 0
while(len(altura) > i):
    a3 = a2
    a2 = a1
    zdeT = altura[i]
    XchapeuMaisUmDadoT = XchapeuT
    pKmaisUmDadoT = pk + Q
    KTmaisUM = (pKmaisUmDadoT)/(pKmaisUmDadoT + R)
    XchapeuTmaisUm = XchapeuMaisUmDadoT +  KTmaisUM*(zdeT - XchapeuMaisUmDadoT)
    pKmaisUm = (1 - KTmaisUM)*(pKmaisUmDadoT)
    pk = pKmaisUm
    XchapeuT = XchapeuTmaisUm
    alturaK.append(XchapeuTmaisUm)
    a1 = XchapeuTmaisUm
    if a1  < a2 :
    	if a2  < a3 :
    		if (a1 - alturaK[0]) > 2: 
    			print("Ponto maximo encontrado em temp[%d], y = %f", i,XchapeuTmaisUm)
    i = i +1
	
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

plt.subplot(221 )
plt.title('aceleracaoZ x tempo ')
plt.plot(temp1, altura)
plt.subplot(222)
plt.title('aceleracaoZk x tempo ')
plt.plot(temp1,alturaK)
#plt.subplot(224)
#plt.plot(temp1,sk)


plt.show()
