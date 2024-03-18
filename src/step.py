from .monitoring import monitoring
from .logs import log_success, log_error, log_wait

@monitoring
def step(function, name:str, retryPolicy:int = 1, errorPolicy:bool = False):
    """Função responsável por facilitar a organização de um flow de trabalho, executando a função com logs 
    pré setados e politica de re-run e tratamento de erro.
    
    OBS: Passar uma env `MONITORING="True"` se quiser verificar dados de execução da função;
    
    - name: Nome do step;
    - retryPolicy: Quantidade de tentativas do step;
    - errorPolicy: Politica de erro, caso True o step pode falhar sem quebrar a aplicação;
    """
    log_wait(f"Iniciando step: {name.upper()} ", log_level="STEP")
    response = None
    for attempt in range(retryPolicy):
        try:
            response = function()
            log_success("Step finalizado com sucesso", log_level="STEP")
            break
        except Exception as e:
            error = e
            log_error(f"Ocorreu um erro ao rodar o step, tentativa: {attempt+1}", log_level="STEP")
    else:
        if errorPolicy:
            log_error(f"Ocorreu um erro durante o step {name}, pulando para o próximo step | erro: {error}", log_level="STEP")
        else:
            log_error(f"Ocorreu um erro durante o step {name}, finalizando aplicação | erro: {error}", log_level="STEP")
            exit(1)
    log_wait(f"Step finalizado: {name.upper()} ", log_level="STEP")
    print("")
    return response
