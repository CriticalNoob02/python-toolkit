from .terminalColor import terminal_color
import os 

try:
    LEVEL = os.environ["LOG_LEVEL"]
except:
    LEVEL = "DEBUG"

def log_error(message:str, log_level:str="DEBUG"):
    """Log vermelho para exibir erros
    - log_level: log será visivel apenas quando o log_level for igual a env LOG_LEVEL
    """
    RESET,COLOR = terminal_color("default","lightRed")
    print(f"{COLOR} {message} {RESET}") if LEVEL.upper() == log_level or LEVEL.upper() == "DEBUG" else None

def log_success(message:str, log_level:str="DEBUG"):
    """Log verde para exibir mensagens de sucesso
    - log_level: log será visivel apenas quando o log_level for igual a env LOG_LEVEL
    """
    RESET,COLOR = terminal_color("default","lightGreen")
    print(f"{COLOR} {message} {RESET}") if LEVEL.upper() == log_level or LEVEL.upper() == "DEBUG" else None

def log_alert(message:str, log_level:str="DEBUG"):
    """Log amarelo para exibir alertas
    - log_level: log será visivel apenas quando o log_level for igual a env LOG_LEVEL
    """
    RESET,COLOR = terminal_color("default","lightYellow")
    print(f"{COLOR} {message} {RESET}") if LEVEL.upper() == log_level or LEVEL.upper() == "DEBUG" else None

def log_wait(message:str, log_level:str="DEBUG"):
    """Log azul para exibir mensagens de espera
    - log_level: log será visivel apenas quando o log_level for igual a env LOG_LEVEL
    """
    RESET,COLOR = terminal_color("default","cyan")
    print(f"{COLOR} {message} {RESET}") if LEVEL.upper() == log_level or LEVEL.upper() == "DEBUG" else None
