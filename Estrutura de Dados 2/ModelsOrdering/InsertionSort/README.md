# Selection Sort

<p align="center"><strong>Versão Otimizada</strong></p>
                                                      
###### 1 - Entrada do usuário para a inserção dos valores no vetor, com um time de iniciador de tempo de execução, um print do vetor inicial e chamada da função order na classe func.py:
<div>  
   <img align="center" src="https://github.com/user-attachments/assets/7a6069b2-3c8a-4cc6-a55a-356e09f3a5b5"/>
</div>
<br>

###### 2 - Função "order" para ordenar, pegando por base o 'i' do primeiro 'for' como menor numero para verificar com o resto do vetor no 'j' do segundo 'for' :
<div>
   <img align="center" src="https://github.com/user-attachments/assets/7a8b8df2-d62b-4036-b572-8608a98f5729"/>
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

