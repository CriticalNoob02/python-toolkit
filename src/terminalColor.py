from .types import Tstyle, Tcolor, Tbase, Tpattern

def terminal_color(style:Tstyle,color:Tcolor) -> tuple[Tbase, Tpattern]:
    """Função privada responsável por criar padrão para uso no terminal;
    """
    style_definition = {"default": "0", "bold": "1", "underlined": "4", "negative": "7"}
    color_definition = {
        "default": "37",
        "black": "30", 
        "red": "31", 
        "green": "32", 
        "yellow": "33", 
        "blue": "34", 
        "magenta": "35", 
        "cyan": "36",
        "lightGray": "37",
        "gray": "90",
        "lightRed": "91",
        "lightGreen": "92",
        "lightYellow": "93",
        "lightBlue": "94",
        "lightMagenta": "95",
        "white": "97"
        }
    base = "\033[0;0m"
    pattern = (f"\033[{style_definition[style]};{color_definition[color]}m")
    return base, pattern
