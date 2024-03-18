from typing import Union, Literal

## Types;
Tstyle = Union[Literal["default"], Literal["bold"], Literal["underlined"], Literal["negative"]]
Tcolor = Union[Literal["default"], Literal["black"], Literal["red"], Literal["green"], 
               Literal["yellow"], Literal["blue"], Literal["magenta"], Literal["cyan"], 
               Literal["lightGray"], Literal["gray"], Literal["lightRed"], Literal["lightGreen"], 
               Literal["lightYellow"], Literal["lightBlue"], Literal["white"]]
Tbase = str
Tpattern = str