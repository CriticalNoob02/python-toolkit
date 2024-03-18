# ToolKit Python
Uma série de ferramentas que foram criadas para cenários diversos.
Todas as funções estão documentadas e em sua maioria tipadas para facilitar a aplicação;

### Ferramentas
- logs -> Sistema de log personalizado e com controle de nivel, onde será printado apenas o que estiver no mesmo nivel que você escolheu dentro da env
- monitoring -> Função decorator para monitorar o consumo de memória e tempo de execução de uma função aplicada;
- multijob -> Função de paralelisação de atividades, para disparar funções simultaneamente, também possui uma função para organizar listas em chunks limitados caso deseje paralelizar uma atividade mas onde cada work faça um trabalho diferente;
- progress -> Função para printar uma barra de progresso, como a atualização do terminal é feita linha a linha na primeira printada sera apagado uma linha anterior e adicionado a barra, então aconselho deixar uma linha em branco antes de iniciar o loop;
- step -> Função wrap para organizar seu ciclo de atividades, onde é possivel repetir a função em casos de erro e tornar a função aderente a falhas sem encerrar seu ciclo;
- terminalColor -> Função para gerar cor ao terminal;

### Exemplos de uso

- Multijob:
```py
# Testando a multitarefa da função;

from src.multiJob import multi_job
import time

def teste(valores:list[int]):
    for valor in valores:
        print(valor)
        time.sleep(1)

multi_job(
    func=teste,
    valores=[1,2,3,4,5,6,7,8,9,10],
    num_works=2)

```
```py
# Testando a multitarefa com divisão de batchs;

from src.multiJob import multi_job
import time

def teste(valores:list[int]):
    for valor in valores:
        print(valor)
        time.sleep(1)

multi_job(
    func=teste,
    rows=[1,2,3,4,5,6,7,8],
    batch_size=4,
    num_works=2)

```

- Progress:
```py
# É possivel mudar o tamanho e a cor da barra de progresso por argumento na função;
from src.progress import progress_bar
import time

steps = ["Alho", "Abobora", "Leite", "Cafe", "Mandioca"]
print("")
for i, item in enumerate(steps):
    progress_bar(
        step=i+1, 
        allSteps=len(steps), 
        message=item,
        # color="lightRed",
        # bar_width=100
        )
    time.sleep(1)

```

- Step:
```py
from src.step import step
import time

def teste(text:str):
    match text:
        case "acertou":
            print(text)
            return 1
        case "errou":
            exit(1)
        case "Errou mas passa bem":
            time.sleep(1)
            raise Exception("abelhas")

func_lamb = lambda: teste("acertou")
value = step(
    function= func_lamb, 
    name= "Função acertando", 
    retryPolicy=3, 
    errorPolicy=True)

func_lamb = lambda: teste("Errou mas passa bem")
value = step(
    function= func_lamb, 
    name= "Função Errando leve", 
    retryPolicy=3, 
    errorPolicy=True)

func_lamb = lambda: teste("errou")
value = step(
    function= func_lamb, 
    name= "Função Errando rude", 
    retryPolicy=3, 
    errorPolicy=True)

```