from typing import List
from ParsedBlocks.ExecutableParsedBlock import ExecutableParsedBlock
from ParsedBlocks.ParsedBlock import ParsedBlock


class FunctionParsedBlock(ParsedBlock):
    def __init__(self, function_identifier: str, parameters: List[str], executable_block: ExecutableParsedBlock) -> None:
        self.function_identifier = function_identifier
        self.parameters = parameters
        self.executable_block = executable_block
        super().__init__()

    def execute(self, var_store: dict) -> None:
        var_store[self.function_identifier.upper()] = self.executable_block
        for parameter in self.parameters:
            if parameter.lower() not in var_store:
                    var_store[parameter.lower()] = 0