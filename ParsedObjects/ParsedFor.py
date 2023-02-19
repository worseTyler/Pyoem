import copy
from typing import List
from ParsedObjects.ParsedObject import ParsedObject


class ParsedFor(ParsedObject):
    def __init__(self, for_operands: List, internal_logic: List) -> None:
        self.internal_logic = internal_logic
        self.for_operands = for_operands
    
    def execute(self, var_store: dict) -> None:
        target_list = var_store[self.for_operands[-1]]
        for i,value in enumerate(target_list):
            if self.for_operands[0] != None:
                var_store[self.for_operands[0]] = i
            var_store[self.for_operands[1]] = value

            logic = copy.deepcopy(self.internal_logic)

            for parsed_object in logic:
                print(var_store)
                parsed_object.execute(var_store)
                
