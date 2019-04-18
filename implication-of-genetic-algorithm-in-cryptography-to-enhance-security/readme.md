O artigo **Implication of Genetic Algorithm in Cryptography to Enhance Security** propõe um algoritmo genético cuja finalidade é gerar chaves seguras para criptografia de dados, através da combinação de caracteres ASCII e números primos. Os autores utilizam a [entropia de Shannan](https://pt.wikipedia.org/wiki/Entropia_da_informa%C3%A7%C3%A3o#Entropia_como_conceito_da_Teoria_da_Informa%C3%A7%C3%A3o) para mensurar a qualidade das chaves geradas, sendo que uma chave é considerada suficientemente segura se a sua entropia for maior ou igual a 0.95.

Neste repositório há o PDF do artigo original e dois scripts escritos na linguagem Python. O `artigo.py` implementa o algoritmo proposto no artigo, enquanto o `basico.py` gera chaves utilizando somente a função `random` padrão da biblioteca Python. A intenção deste repositório é verificar se o algoritmo proposto no artigo realmente gera chaves mais seguras.

O algoritmo proposto no artigo foi executado um milhão de vezes. O gráfico abaixo mostra quantas gerações foram necessárias pra obter-se uma chave suficientemente segura (isto é, uma chave com entropia maior ou igual a 0.95).

![alt text](./grafico-1.png)
