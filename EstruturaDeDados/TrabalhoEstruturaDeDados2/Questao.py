import csv
from typing import List
import timeit 

def busca_linear(nome: str, servidores_dns: List[dict]) -> List[dict]:
    ipsServidor = []
    for i in range(len(servidores_dns)):
        if nome == servidores_dns[i]['nome']:
            ipsServidor.append(servidores_dns[i])
    return ipsServidor

def busca_linear_recursiva(nome: str, servs: List[dict], servidoresEncontrados: List=[]) -> List[dict]: 
    if len(servs) == 0 or nome < servs[0]['nome']:
        return servs

    if nome == servs[0]['nome']:
        servidoresEncontrados.append(servs[0])

    servs.pop(0)
    busca_linear_recursiva(nome, servs)
    
    return servidoresEncontrados

servidores_dns = []
with open('dns_br.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  next(csv_reader, None)  # pula os cabeçalhos
  for row in csv_reader:
    servidor_dns = dict()
    servidor_dns['ip'] = row[0]
    servidor_dns['nome'] = row[1]
    servidores_dns.append(servidor_dns)

for i in servidores_dns:
    i['nome'] = i['nome'].upper()

print(servidores_dns)
print('***** Ordenados *****')
#print(ordenarServidores(servidores_dns))
servidores_dns.sort(key=lambda k:k['nome'])
print(servidores_dns)

empresa = input('Digite a organização desejada: ')
print('*** Resultados de ips da ' + str(empresa.upper()) + ' ***')

#for i in busca_linear_recursiva(empresa.upper(), servidores_dns):   
 #   print(i['ip'])

print('BuscaLinear')
for j in busca_linear(empresa.upper(), servidores_dns):
    print(j['ip'])
print('Busca recursiva')
for i in busca_linear_recursiva(empresa.upper(), servidores_dns):   
    print(i['ip'])
