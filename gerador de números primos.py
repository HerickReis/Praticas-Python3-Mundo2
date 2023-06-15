'''Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.'''

'''passo a passo:
Claro! Vou explicar o script passo a passo de forma didática para um iniciante entender melhor:

1. O programa começa pedindo ao usuário para inserir um número inteiro.

2. Em seguida, usamos um loop `while` externo para iterar sobre os números de 1 até o número digitado pelo usuário (representado pela variável `n`).

3. Dentro desse loop `while`, temos uma variável chamada `num` que começa em 1. Essa variável representa cada número que estamos testando para verificar se é primo.

4. Criamos uma variável chamada `divisors` e a inicializamos com o valor 0. Essa variável será usada para contar quantos divisores o número `num` possui.

5. Em seguida, temos outro loop `while` interno. Esse loop vai de 1 até o valor de `num` e é usado para verificar todos os possíveis divisores do número `num`.

6. Dentro do loop interno, verificamos se o número `num` é divisível por `i` (o valor atual do loop). Se a divisão resultar em resto zero, significa que `i` é um divisor de `num` e incrementamos a variável `divisors` em 1.

7. Após o término do loop interno, verificamos se o valor de `divisors` é igual a 2. Se for, significa que o número `num` possui exatamente dois divisores (1 e ele mesmo), o que é a condição para ser um número primo.

8. Se `divisors` for igual a 2, imprimimos o valor de `num`, pois ele é um número primo. Caso contrário, passamos para o próximo número.

9. Incrementamos a variável `num` em 1 para passar para o próximo número e repetimos o processo.

10. O programa continua executando até que `num` alcance o valor de `n`, ou seja, até que tenhamos verificado todos os números no intervalo.

11. Por fim, o programa imprime todos os números primos encontrados.

Espero que essa explicação passo a passo ajude a entender o funcionamento do script!'''

n = int(input('Informe um número inteiro: '))

print('Números primos encontrados')
num = 1
while num <= n:
    divisores = 0
    i = 1

    while i <= num:
        if num % i == 0:
            divisores += 1
        i += 1

    if divisores == 2:
        print(num,end=" ")

    num += 1