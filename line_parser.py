if __name__ == "__main__":
    # opParser = OperatorParser()
    # args = [
    #         ["saltly, quack var!"],
    #         ["quack fish!"],
    #         ["one, three fiver!"],
    #         ["three fiver!"]  
    #     ]
    # for arg in args:
    #     store = {
    #         "quack": 56,
    #         "last_value": 4
    #     }
    #     parsedOperator = opParser.parse(arg)
    #     if parsedOperator is not None:
    #         parsedOperator.execute(store)
    #         print(store)

    def tests_operations():
        tests = [
            ("Collin, fish sto!", {'Collin': 3}), # store
            ("fish cach!", {'last_value': 3}), # cache
            ("five, one addss!", {'last_value': 5}), # add
            ("five, one subsss!", {'last_value': 1}), # sub
            ("12345, 123 1234567!", {'last_value': 8}), # mul
            ("012345678, 01234 12345678!", {'last_value': 2}), # div
            ("01234, 01235 123456789!", {'last_value': True}), # equals
            ("01234, 01 123456789!", {'last_value': False}), # equals
            ("Collin, fish 1234567890!", {'last_value': True}), # greater
            ("fish, Collin  1234567890!", {'last_value': False}), # greater
            ("Collin, fish 12345678901!", {'last_value': False}), # less
            ("fish, Collin  12345678901!", {'last_value': True}), # less
            # ("Collin, fish fiver!", {'last_value': 3}), # negate
            # ("Collin, fish fiver!", {'last_value': 3}), # or
            # ("Collin, fish fiver!", {'last_value': 3}), # and
        ]

        for test in tests:
            opParser = OperatorParser()
            parsedOperator = opParser.parse([test[0]])
            if parsedOperator is not None:
                expected = copy.deepcopy(test[1])
                parsedOperator.execute(test[1])

                print("START")
                print(test[1])
                print(f"Result: {expected == test[1]}\n\n")
    
    # tests_operations()

    def tests_conditional():
            tests = [
                (["Condition?", "result, fishy, yum!", "It can be anything."], {'last_value': True}, {'result': 4, 'last_value': True}), # true case
                (["Condition?", "result, fishy, yum!", "It can be anything."], {'last_value': False}, {'last_value': False}), # false case
            ]
            
            for test in tests:
                opParser = ConditionalParser()
                parsed_object = opParser.parse(test[0])
                if parsed_object is not None:
                    expected = copy.deepcopy(test[2])
                    parsed_object.execute(test[1])

                    print("START")
                    print(test[1])
                    print(f"Result: {expected == test[1]}\n\n")
        
    tests_conditional()
