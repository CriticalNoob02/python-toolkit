import os
from functools import wraps
import tracemalloc
from time import perf_counter

try:
    MONITOR = os.environ["MONITORING"]
except:
    MONITOR = "False"

def monitoring(func):
    """Decorator responsável por gerar dados de monitoria na função aplicada;
    env: `MONITORING="True"`
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if MONITOR == "True":
            tracemalloc.start()
            start_time = perf_counter()
            result = func(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            finish_time = perf_counter()
            print(f'{"-"*40}')
            print(f'Função: {func.__name__}')
            print(f'Uso de memória:\t\t {current / 10**6:.6f} MB')
            print(f'Uso máximo de memória:\t {peak / 10**6:.6f} MB ')
            print(f'Tempo de execução:\t {finish_time - start_time:.6f} S')
            print(f'{"-"*40}')
            tracemalloc.stop()
            return result
        else:
            return func(*args, **kwargs)
    return wrapper
