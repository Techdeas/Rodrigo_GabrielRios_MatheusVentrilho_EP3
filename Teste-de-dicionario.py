"""
Projeto 3:
Grupo:
    Babriel Rios
    Matheus
    Rodrigo Lopes
"""
import matplotlib.pyplot as plt 


#-----------------------------------------------------------------------------#
#Parte que organiza o arquivo alimentos.csv em 5 dicionarios:
#OBS: Todos os dados estao no formato str
arquivo1 = open("alimentos.csv", encoding="latin1")

lista1 = arquivo1.readlines()
dicquant = {}
diccal = {}
dicprot = {}
diccarbo = {}
dicgord = {}
listadic = [dicquant, diccal , dicprot , diccarbo , dicgord] 

for i in range(1 , len(lista1)):
    elementos = str(lista1[i])
    elementos = elementos.split(',')
    
    for j in range(0, len(elementos)-1):
        
        dic = listadic[j]
        dic[elementos[0]] = float(elementos[j+1])

#print(sorted(diccal.keys()))
#print(dicquant)

#-----------------------------------------------------------------------------#
#Parte que organiza o arquivo  usuario.csv em dados e dicionarios:
#OBS: Todos os dados estao no formato str
#from collections import defaultdict

arquivo2 = open("usuario.csv", encoding='utf-8')
lista2 = arquivo2.readlines()

data = []
dict = {}
dicquant2 = {}
dicativ = {}
dicmet = {} 

dados = str(lista2[1]).split(',')

nome =   dados[0]
idade =  int(dados[1])
peso =   float(dados[2])
sexo =   dados[3]
altura = float(dados[4])
fator =  dados[5]

#Organiza alimento de acordo com o dia! 
#----------------------------------------------------------------#             
for i in range(3, len(lista2)):                                  #
    info = str(lista2[i])                                        #
    info = info.split(',')                                       #
                                                                 #
    if info[0] not in data:                                      #
        data.append(info[0])                                     #
    for j in range(0,len(info)-2):                               #
        dict[info[1]] = info[0]                                  #
        dicquant2[info[1]] = float(info[2]) #proteinas           #
                                                                 #
new_dict = {}                                                    #
for pair in dict.items():                                        #
    if pair[1] not in new_dict.keys():                           #
        new_dict[pair[1]] = []                                   #
                                                                 #
    new_dict[pair[1]].append(pair[0])                            #


#----------------------------------------------------------------------------#
#Abrindo o arquivo 3 com a tabela de atividades!
arquivo3 = open('atividades.csv')
lista3 = arquivo3.readlines()

dicativ = {}

for i in range(1,len(lista3)):
    ativ = str(lista3[i])
    ativ = ativ.split(',')
    for j in range(0,len(ativ)):
        dicativ[ativ[0]] = float(ativ[1])

#----------------------------------------------------------------------------#
#Abrindo o arquivo 4 com os exercicios feitos pelo usuário!
arquivo4 = open('exercicios.csv',encoding="latin1")
lista4 = arquivo4.readlines()

dict_1 = {} #Dicionário que irá conter o exercicio e o dia que foi feito
dicexmin = {} #Dicionário que irá conter o exercício e quantos minutos ele durou
dataex = []



for i in range(1,len(lista4)):
    exerc = str(lista4[i])
    exerc = exerc.split(',')
    if exerc[0] not in dataex:                                      #
        dataex.append(exerc[0]) 
    for j in range(0,len(exerc)):
        dict_1[exerc[1]] = exerc[0]
        dicexmin[exerc[1]] = float(exerc[2])
        
new_dict_1 = {}                                                    #
for pair in dict_1.items():                                        #
    if pair[1] not in new_dict_1.keys():                           #
        new_dict_1[pair[1]] = []                                   #
                                                                   #
    new_dict_1[pair[1]].append(pair[0])   

dataex = sorted(dataex)
perda = 0
perdatot = []
for x in range(0, len(dataex)):
    lista_1 = new_dict_1[dataex[x]]
    for y in range(0,len(lista_1)):
        perda += (dicativ[lista_1[y]]*peso)*(dicexmin[lista_1[y]]/60)
    perdatot.append(perda)
    perda = 0
    


cal = 0
prot = 0
carbo = 0
gord = 0
caltotal  = []  
prottotal=[]
carbototal = []
gordtotal = []

data = sorted(data)

for x in range(0, len(data)):
    lista = new_dict[data[x]]

    for y in range(0,len(lista)):
        cal += ((diccal[lista[y]]*dicquant2[lista[y]])/100)
        prot+=(dicprot[lista[y]]*dicquant2[lista[y]])/100
        carbo+=(diccarbo[lista[y]]*dicquant2[lista[y]])/100
        gord+=(dicgord[lista[y]]*dicquant2[lista[y]])/100
    prottotal.append(prot)  #Lista com os valores de proteínas
    caltotal.append(cal)   #Lista com os valores de calorias
    carbototal.append(carbo) #Lista com os valores de carboidratos
    gordtotal.append(gord) #Lista com os valores de gorduras
    
    
    prot=0
    cal=0
    carbo = 0
    gord = 0

for x in range(0, len(data)):
    for y in range(0, len(dataex)):
        if data[x] == dataex[y]:
            caltotal[x]-=perdatot[y]
#print(data)
#print(caltotal)

dias = []    
    
for q in range(0, len(data)):
    datast = data[q]
    datast = datast.split('/')
    dias.append(float(datast[0]))


#----------------------------------------------------------------------------#


#Calculo da quantidade necessaria de calorias diarias:
dicfator = {'baixo':1.375, 'medio':1.55, 'alto':1.725, 'muito alto':1.9}
TBM = 0

if sexo == 'M':
    TBM += 88.36+(13.4*peso)+(4.8*(altura*100)-(5.7*idade))
elif sexo == 'F': 
    TBM += 447.6+(9.2*peso)+(3.1*(altura*100)-(4.3*idade))

fat = dicfator[fator[0:-1]]
TBM = TBM*fat

print(TBM) #TBM é o valor ideal de calorias 



plt.plot(dias, caltotal) 
plt.axis([dias[0], max(dias), min(caltotal), max(caltotal)]) 
plt.ylabel('Dia') 
plt.xlabel('Quantidade de calorias') 
plt.title(r'Quantidade de calorias consumidas por dia') 
plt.show()





    



