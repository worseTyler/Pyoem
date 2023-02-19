from typing import List

from util import Util

class Operations():
    def store(operands: List[str], var_store: dict):
        if not len(operands) in [1,2]:
            raise SyntaxError("HOW DARE YOU")

        if len(operands) == 1:
            operands.insert(0, 'last_value')

        var_store[operands[0]] = Util.eval_operand(operands[1], var_store)

    def cache(operands: List[str], var_store: dict):
        if len(operands) != 1:
            raise SyntaxError("HOW DARE YOU")


        var_store[operands[0].strip()] = var_store['last_value']

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

    def mod(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] % operands[1]

    def equals(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
                
        operands = Operations.setup_operands(operands, var_store)

        var_store["last_value"] = operands[0] == operands[1]

    def greater(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] > operands[1]

    def less(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] < operands[1]

    def negate(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        if len(operands) == 0:
            operands.append(operands[0])
            operands[0] = "last_value"    

        operands[0] = Util.eval_operand(operands[0], var_store)

        var_store["last_value"] = not operands[0] 

    def op_and(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] and operands[1]

    def op_or(operands: List[str], var_store: dict):
        if len(operands) != 1 and len(operands) != 2:
            raise SyntaxError("HOW DARE YOU")
        
        operands = Operations.setup_operands(operands, var_store)
        var_store["last_value"] = operands[0] or operands[1]

    def op_print(operands: List[str], var_store: dict):
        if len(operands) > 1:
            raise SyntaxError("HOW DARE YOU")
        
        if len(operands) == 0:
            operands.append('last_value')

        eval = Util.eval_operand(operands[0], var_store)
        print(eval)

    def op_read(operands: List[str], var_store: dict):
        if len(operands) > 1:
            raise SyntaxError("HOW DARE YOU")
        
        if len(operands) == 0:
            operands.append('last_value')

        var_store[operands[0]] = input(": ")