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
            4: Operations.store,
            5: Operations.cache,

            6: Operations.op_print,
            7: Operations.op_read,

            8: Operations.add,
            9: Operations.sub,
            10: Operations.mul,
            11: Operations.div,
            12: Operations.mod,

            13: Operations.equals,
            14: Operations.greater,
            15: Operations.less,
            16: Operations.negate,
            17: Operations.op_and,
            18: Operations.op_or,

            19: Operations.index,
        }
    
    def execute(self, var_store: dict) -> None:
        operation_length = len(self.operation_token)
        if operation_length not in self.operation_dict:
            raise SyntaxError(f"Why do you think {self.operation_token} qualifies as literature")
        operation_function = self.operation_dict[operation_length]
        operation_function(self.operands, var_store)
        # print(evaluated_operands)