import copy
from typing import List
from ParsedBlocks.ExecutableParsedBlock import ExecutableParsedBlock
from ParsedObjects.ParsedObject import ParsedObject
from util import Util


class ParsedFunctionCall(ParsedObject):
    def __init__(self, function_identifier: str, parameters: List[str]) -> None:
        self.function_identifier = function_identifier
        self.parameters = parameters
    
    def execute(self, var_store: dict) -> None:
        param_names = self.function_identifier.lower().split(' ')
        for index, value in enumerate(param_names):
            if len(self.parameters) < index:
                break
            var_store[value.strip()] = Util.eval_operand(self.parameters[index], var_store)
        print(var_store)
        executable_block = var_store[self.function_identifier.strip()]
        if not type(executable_block) == ExecutableParsedBlock:
            raise SyntaxError("The quoted material is irrelevant.")
        executable_block.execute(var_store)
                
