# Insertion Sort

<p align="center"><strong>Versão Otimizada</strong></p>
                                                      
###### 1 - Entrada padrão do sistema com valores desordenados, início do 'time' para saber o tempo de execução do programa, quantidades passadas como tam[0], print do vetor desordenado e chamada da função order na classe func.py:
<div>  
   <img align="center" src="https://github.com/user-attachments/assets/41ac74cf-c91a-4f85-a8ae-73a3f2087467"/>
</div>
<br>

###### 2 - Na função order, pega-se o tamanho do vetor para as passadas necessárias, resgatando o valor da primeira posição 'i' juntamente com um 'j -1' da iteração atual, sendo assim, entrando no 'While' para que seja executado a verificação ate 'j' for >= 0 e o vetor da porsição 'j' for maior que o valor da iteração de 'i', fazendo a troca ate encontrar um valor maior que ele ou 'j' ser igual a -1, sendo assim ordenando conforme o necessário, contabilizando o número de passadas:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/9cef2ac3-45df-4932-9f72-b6004dcc7fad"/>
</div>
<br>

###### 3 - Após a verificação do menor numero da lista, faz-se a troca adequada para a ordem crescente, verificando assim se o 'i != x' para que não ocorra comparações desnecessárias para um melhor desempenho e tempo de execução, evitando uso de memória excessivo:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/3d263895-1a50-4bb2-bb71-92ee6df88132"/>
</div>

###### 4 - Saída final, apresentando o vetor em ordem crescente, número de iterações e o tempo de execução:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/6589976a-de6d-4d79-bbe6-dc676bddf5d9"/>
</div>

###### 5 - Resultado da saída final, com 5 iterações e cerca de 5 segundos de execução:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/3b9e1058-c85a-41b2-881d-6e358e74a41d"/>
</div>
<br>

<p align="center"><strong>Versão NÂO Otimizada</strong></p>

###### 1 - Todo o processo inicial é o mesmo da versão otimizada, porém com uma diferença de iteração na classe "func.py", sem a verificação se o 'i != x', sendo assim tendo mais iterações desncessárias com valores que não precisam ser mais verificados:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/0a74fdce-a17e-4b48-805a-eed7e359c5f7"/>
</div>
<br>

###### 2 - Sáida com um aumento de iterações para 10 vezes e tempo de execução quase 2 segundos a mais, ocupando mais espaço no uso de memória:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/22e74f21-2efd-472f-a52a-2a99b8446916"/>
   <img align="center" src="https://github.com/user-attachments/assets/75ceb81f-f2bf-4f12-afa8-0cbd25122e3b"/>
</div>
<br>

<p align="center"><strong>Conclusão</strong></p>

###### A versão otimizada contém um método de verificação para evitar comaprações desncessárias com valores já ordenadas, diminuindo a metade das iterações e com tempo de execução menor, já a versão NÂO otimizada, com o dobro de iterações , elevando mais o tempo de execução, propriamente dito que o programa fica mais lento.

