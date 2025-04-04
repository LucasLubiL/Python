# Insertion Sort

<p align="center"><strong>Versão Otimizada</strong></p>
                                                      
###### 1 - Entrada padrão do sistema com valores desordenados, início do 'time' para saber o tempo de execução do programa, quantidades passadas como tam[0], print do vetor desordenado e chamada da função order na classe func.py:
<div>  
   <img align="center" src="https://github.com/user-attachments/assets/41ac74cf-c91a-4f85-a8ae-73a3f2087467"/>
</div>
<br>

###### 2 - Na função order, pega-se o tamanho do vetor para as passadas necessárias, resgatando o valor da primeira posição 'i' juntamente com um 'j -1' da iteração atual, sendo assim, entrando no 'While' para que seja executado a verificação ate 'j' for >= 0 e o vetor da porsição 'j' for maior que o valor da iteração de 'i', fazendo a troca ate encontrar um valor maior que ele ou 'j' ser igual a -1(Juntamente com um print mostrando as trocas sendo feitas), sendo assim ordenando conforme o necessário, contabilizando o número de passadas:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/f93ee284-3ea4-43e9-853d-7ddb4f3158a1"/>
</div>
<br>

###### 3 - Preparação para a saída final, com o vetoro ordenado, quantidades passadas em trocas e o tempo de execução do sistema:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/53a3c1a0-0bb7-4fd9-af0c-59f94d58f1e4"/>
</div>

###### 4 - Resultado final, com 3 iterações e tempo de execução o mínimo possível:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/dc413679-6439-4f78-8848-b55e57bf673f"/>
</div>

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

