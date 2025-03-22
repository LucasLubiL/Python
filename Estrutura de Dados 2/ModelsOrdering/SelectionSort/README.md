# Selection Sort

<p align="center"><strong>Versão Otimizada</strong></p>
                                                      
###### Entrada do usuário para a inserção dos valores no vetor, com um time de iniciador de tempo de execução, um print do vetor inicial e chamada da função order na classe func.py:
<div>  
   <img align="center" src="https://github.com/user-attachments/assets/7a6069b2-3c8a-4cc6-a55a-356e09f3a5b5"/>
</div>
<br>

###### Função "order" para ordenar, pegando por base o 'i' do primeiro 'for' como menor numero para verificar com o resto do vetor no 'j' do segundo 'for' :
<div>
   <img align="center" src="https://github.com/user-attachments/assets/7a8b8df2-d62b-4036-b572-8608a98f5729"/>
</div>
<br>

###### Após a verificação do menor numero da lista, faz-se a troca adequada para a ordem crescente, verificando assim se o 'i != x' para que não ocorra comparações desnecessárias para um melhor desempenho e tempo de execução, evitando uso de memória excessivo:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/3d263895-1a50-4bb2-bb71-92ee6df88132"/>
</div>

###### Resultado da saída final:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/a7fe4904-2644-4ffa-a1da-50e7594fc693"/>
</div>
<br>

<p align="center"><strong>Versão NÂO Otimizada</strong></p>

###### Todo o processo inicial é o mesmo da versão otimizada, porém com uma diferença de iteração na classe "func.py", aumentando a quantidade de verificações no 'for' após elimiar o -i:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/1af230e5-4696-4065-b714-f73be3fecec3"/>
</div>
<br>

###### Sáida com um aumento de iterações para 81 vezes, ocupando mais espaço no uso de memória:
<div>
   <img align="center" src="https://github.com/user-attachments/assets/c3127baf-0f03-4036-9a1a-db5c3538af2c"/>
</div>
<br>

<p align="center"><strong>Conclusão</strong></p>

###### Vemos que a versão otimizada consequentemente é melhor, pois nela se tem menas iterações, ou seja, menos espaço de memória usada, enquanto a não ptimizada é quase o dobro de iterações com mais uso de espaço de memória, sendo ineficaz, deixando a execução mais lenta do que deveria ser.




