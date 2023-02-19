if __name__ == "__main__":
    # tests = [
    #     ['alphabet,', 'numeral,', '-Tyler'],
    #     ['alphabet,', '-Tyler'],
    #     ["'alphabet',", '-Tyler']
    # ]

    # for test in tests:
    #     print("Start Test")

    #     var_store = {}
    #     declarationParser = DeclarationParser(test)
    #     block = declarationParser.parse()
    #     var_store = block.execute(var_store)
    #     print(var_store)   

    #     print("End Test\n") 

    
    tests = [
            [
                'one, fish fiver!',
                'fish fish!'
                ]
        ]

    for test in tests:
        print("Start Test")

        var_store = {}
        parser = ExecutableParser()
        block = parser.parse(test)
        block.execute(var_store)
        print(var_store)

        print("End Test\n")
        
        


