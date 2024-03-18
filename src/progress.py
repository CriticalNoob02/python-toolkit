from .terminalColor import terminal_color
from .types import Tcolor

def progress_bar(step:int, allSteps:int, message:str, bar_width:int=50, color:Tcolor="white") -> None:
    """Função responsável por gerar uma barra de progresso no terminal
    - step: Valor atual do progresso;
    - allSteps: Valor total do progresso;
    - message: Nome do estado atual do progresso;
    - bar_width: Tamanho da barra de progresso;
    - color: Cor da barra de progresso no terminal;

    OBS: Por padrão a barra substitui uma linha printada antes de iniciar o processo,
    por isso é recomendado adicionar um `print("")` antes do inicio do loop onde será inserido a barra.
    """
    BASE, COLOR = terminal_color("default", color)
    percent = step / allSteps
    barsAmount = int(percent * bar_width)
    bars = "█" * barsAmount
    spaces = " " * (bar_width - barsAmount)

    print(f"\033[F\033[K{COLOR}Worker |{bars}{spaces}| {int(percent * 100)}% -- {message}{BASE}")
