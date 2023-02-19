from typing import List

from util import Util

class Operations():
    def store(operands: List[str], var_store: dict):
        print(operands)
        if len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")

        var_store[operands[0]] = Util.eval_operand(operands[1], var_store)

    def cache(operands: List[str], var_store: dict):
        print(operands)
        if len(operands) != 1:
            raise SyntaxError("HOW DARE YOU")
        
        var_store["last_value"] = Util.eval_operand(operands[0], var_store)

    def add(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")

        operands[0] = Util.eval_operand(operands[0], var_store)
        operands[1] = Util.eval_operand(operands[1], var_store)

        var_store["last_value"] = operands[0] + operands[1]