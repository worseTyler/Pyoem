from LineParsers.ForParser import ForParser
from LineParsers.OperatorParser import OperatorParser
from LineParsers.ConditionalParser import ConditionalParser
import copy

line_parsers = [
    OperatorParser(),
    ConditionalParser(),
    ForParser(),
]
def tests_operations():
    tests = [
        ("Collin, fish, stop!", {'Collin': 3}), # store
        ("fish, swims!", {'last_value': 3}), # cache
        ("five, one, I am add!", {'last_value': 5}), # add
        ("five, one, subtracts!", {'last_value': 1}), # sub
        ("12345, 123, multiplies!", {'last_value': 8}), # mul
        ("012345678, 01234, 12345678901!", {'last_value': 2}), # div
        ("01234, 01235, 1234567890123!", {'last_value': True}), # equals
        ("01234, 01, 1234567890123!", {'last_value': False}), # equals
        ("Collin, fish, 12345678901234!", {'last_value': True}), # greater
        ("fish, Collin,  12345678901234!", {'last_value': False}), # greater
        ("Collin, fish, 123456789012345!", {'last_value': False}), # less
        ("fish, Collin,  123456789012345!", {'last_value': True}), # less
    ]

    for test in tests:
        opParser = OperatorParser()
        parsedOperator = opParser.parse([test[0]], line_parsers)
        if parsedOperator is not None:
            expected = copy.deepcopy(test[1])
            parsedOperator.execute(test[1])

            print("START")
            print(test[1])
            print(f"Result: {expected == test[1]}\n\n")

tests_operations()

def tests_conditional():
        tests = [
            (["Condition?", "result, fishy, I am add!", "It can be anything."], {'last_value': True}, {'result': 4, 'last_value': True}), # true case
            (["Condition?", "result, fishy, I am add!", "It can be anything."], {'last_value': False}, {'last_value': False}), # false case
            (["Condition?", "Condition?", "result, fishy, I am add!", "It can be anything.", "But it isn't."], {'last_value': True}, {'last_value': True, 'result': 9}), # nested case
        ]
        

tests_conditional()

def tests_for():
        tests = [
            (["For...", "value list", "value, I am add!", "I wasn't listening."], {'last_value': 0, 'list': [1,2,3,4]}, {'last_value': 10, 'list': [1,2,3,4], 'value': 4}), # basic case   
            (["For...", "index value list", "value, I am add!", "I wasn't listening."], {'last_value': 0, 'list': [1,2,3,4]}, {'last_value': 10, 'list': [1,2,3,4], 'value': 4, 'index': 3}), # index case
            (["For...", "value list", "For...", "item list", "item, I am add!", "End block.", "value, I am add!", "I wasn't listening."], {'last_value': 0, 'list': [1,2,3,4]}, {'last_value': 50, 'list': [1,2,3,4], 'value': 4, 'item': 4}), # nested case              
        ]
        
        for test in tests:
            opParser = ForParser()
            parsed_object = opParser.parse(test[0], line_parsers)
            if parsed_object is not None:
                expected = copy.deepcopy(test[2])
                parsed_object.execute(test[1])

                print("START")
                print(test[1])
                print(f"Result: {expected == test[1]}\n\n")
    
tests_for()
