import multiprocessing
from .logs import log_wait

def batch_organizer(rows:list, batch_size:int, num_works:int) -> tuple[list, int, int]:
    """Função responsável por organizar igualmente a lista de informação entre batchs limitados
    
    return = 1º lista dividida, 2º quantidade de repetições, 3º Sobras
    """
    divided_list = [rows[i:i+batch_size] for i in range(0, len(rows), batch_size)]
    repetition = len(divided_list) // num_works
    remaining = len(divided_list) % num_works
    log_wait(f"Quantidade de vezes que cada work vai rodar uma lista: {repetition}")
    log_wait(f"Listas que não entraram na distribuição igualitária de works: {remaining}")
    return divided_list, repetition, remaining


def multi_job(func, batch_size:int=None, rows:list=None, num_works:int=1, *args, **kwargs):
    """Função responsável por gerar trabalho em paralelo usando multiprocessos;
    OBS: A função enviada deve manter a lista como primeiro argumento

    - func: Função que deseja rodar, sem argumentos nem parenteses;
    - num_works: Números de funções em paralelo;
    - batch_size?: `Caso deseje separar em batchs` definição do tamanho de cada lista;
    - rows?: `Caso deseje separar em batchs` lista completa a ser dividida;
    - *args e **kwargs: Argumentos e chaves da função que deseja passar; 

    OBS: Está função tem a capacidade de dividir alguma lista em batchs definidos para o trabalho em paralelo com dados diferentes;
    """
    # Separação de batch;
    if batch_size != None:
        divided_list, repetition, _ = batch_organizer(rows=rows, batch_size=batch_size, num_works=num_works)

        # Iniciando processos paralelos por works;
        for _ in range(repetition):
            processes = [multiprocessing.Process(target=func, args=(args + (chunk,)), kwargs=kwargs) for chunk in divided_list[:num_works]]
            for process in processes:
                process.start()
            for process in processes:
                process.join()
            divided_list = divided_list[num_works:]

        # Iniciando processos restantes;
        processes = [multiprocessing.Process(target=func, args=(args + (chunk,)), kwargs=kwargs) for chunk in divided_list]
        for process in processes:
            process.start()
        for process in processes:
            process.join()

    # Caso não precise de batch
    else:
        processes = [multiprocessing.Process(target=func, args=args, kwargs=kwargs) for _ in range(num_works)]
        for process in processes:
            process.start()
        for process in processes:
            process.join()
