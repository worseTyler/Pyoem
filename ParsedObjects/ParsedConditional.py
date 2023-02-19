from typing import List
from ParsedObjects.ParsedObject import ParsedObject


class ParsedConditional(ParsedObject):
    def __init__(self, internal_logic: List) -> None:
        self.internal_logic = internal_logic
    
    def execute(self, var_store: dict) -> None:
        if var_store['last_value']:
            for parsed_object in self.internal_logic:
                parsed_object.execute(var_store)