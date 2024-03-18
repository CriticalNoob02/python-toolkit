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
