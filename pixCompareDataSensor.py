import csv
import matplotlib.pyplot as plt
import math
## script comparacao dos dados do mesmo sensor em leituras diferentes 

##         localizacao do arquivo com os dados do arquivo1
f2 = open('17_21_02_vehicle_air_data_0.csv ', 'r' )


##         localizacao do arquivo com os dados do arquivo2
f = open('17_21_02_sensor_combined_0.csv', 'r' )
f.close()
##	vetores da leitura 1 
temp1  = []
roll1  = []
pitch1 = []
yaw1   = []
## 	vetores da leitura 2 

altura = []
	
leitor2 = csv.reader(f2)
leitor = csv.reader(f)
#leitor2 = csv.reader(f2)
cont  = 0 ## contadores pra saltar linhas com texto


cont = 0

for linha in leitor2:
   if  cont == 0 :
      cont = cont + 1
   else :
       temp1.append(cont-1)
       altura.append(float(linha[1]))
       cont = cont +1


plt.subplot(2, 1, 1)
plt.plot(temp1,roll1)
plt.plot(temp1,altura)

plt.title('altura x tempo ')
plt.ylabel('altura')
plt.xlabel('time ')

plt.show()


