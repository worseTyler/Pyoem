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

        eval = Util.eval_operand(operands[0], var_store)
        var_store["last_value"] = eval

    def setup_operands(operands, var_store):
        if len(operands) == 1:
            operands.append(operands[0])
            operands[0] = "last_value"    

        operands[0] = Util.eval_operand(operands[0], var_store)
        operands[1] = Util.eval_operand(operands[1], var_store)

        return operands        

    def add(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] + operands[1]

    def sub(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] - operands[1]

    def mul(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] * operands[1]

    def div(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] / operands[1]

    def equals(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] == operands[1]
        