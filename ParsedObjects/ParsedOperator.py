from typing import List
from ParsedObjects.ParsedObject import ParsedObject
from operations import Operations
from util import Util
import copy

class ParsedOperator(ParsedObject):

    def __init__(self, operation_token: str, operands: List[str]) -> None:
        self.operation_token = operation_token
        self.operands = operands
        self.operation_dict = {
            3: Operations.store,
            4: Operations.cache,
            5: Operations.add,
            6: Operations.sub,
            7: Operations.mul,
            8: Operations.div,
            9: Operations.equals,
            10: Operations.greater,
            11: Operations.less,
            12: Operations.negate,
            13: Operations.op_and,
            14: Operations.op_or
        }
    
    def execute(self, var_store: dict) -> None:
        operation_length = len(self.operation_token)
        if operation_length not in self.operation_dict:
            raise SyntaxError(f"Why do you think {self.operation_token} qualifies as literature")
        operation_function = self.operation_dict[operation_length]
        operation_function(self.operands, var_store)
        # print(evaluated_operands)