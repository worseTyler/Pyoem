# Pyoem

## Team 4 People (Tyler, Collin, Nick, Anna)

Pyoem is a new programming language created during the 2023 WSU Hackathon. It provides the option for developers to write their projects in Poems. Operators, Declarations, and Function Calls are all supported.

## Special  Terms

| Term      | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| Stanza    | A block of logic in Pyoem                                    |
| Verse     | A section of logic in Pyoem, generally contained in a stanza. Verses may include other verses. |
| [[0-9].*] | A word or phase of same length of characters. For example, [6] = poetry = my pup. |

## Numbers

In Pyoem, each digit is evaluated as the length of the word - 1. Multidigit number are expressed by multiple words that correspond to each digit.

| Pyoem     | Meaning |
| --------- | ------- |
| apple     | 4       |
| apple pie | 42      |

## User Defined  Variables

You can create defined variables in Pyoem. The syntax for this is the value then followed on a newline by "-nameOfNewVariable". If you want to declare a list, separate the values by a comma and a newline, then conclude with a "-name". Pyoem supports integers, strings, and lists of strings or ints. For example:

| Pyoem     | Meaning                                         |
| --------- | ----------------------------------------------- |
| 0         | This evaluates to the number 0                  |
| -hasWon   | This sets the value of 0 to the variable hasWon |
|           |                                                 |
| 'example' | This evaluates to the string "example"          |
| -newVar   | This sets the value of 'example' to newVar      |

## Operations

Pyoem supports common operations that vary from reading and writing to arithmetic to inequalities. The following table provides a reference for operations that you can preform in Pyoem. The operation lines are written in postfix so the structure of an operation statement is [ (parameter set, spaced by commas) , (operation ref)!], for example to add 2 and 7 the operation line would read as - [3], [8], [8]!  which is equal to sun, balloon, umbrella!

| Index | Definition                       | Description                                                  | Example            |
| ----- | -------------------------------- | ------------------------------------------------------------ | ------------------ |
| 4     | store(dest, src); store(src)     | Stores the value of src in dest. If only src provided, src is stored in last_value | dest, src, [4]!    |
| 5     | cache(dest)                      | Stores the value of last_value in dest                       | dest, [5]!         |
| 6     | print(src); print()              | Prints the value of src. If no parameter given, prints the value of last_value | src, [6]!          |
| 7     | read(dest); read()               | Stores the user's input in dest. If no parameter given, stores the user's input in last_value | dest, [7]!         |
| 8     | add(op1, op2);                   | Adds op1 and op2 then stores the value in last_value         | op1, op2, [8]!     |
| 9     | sub(op1, op2)                    | Subtracts op1 and op2 then stores the value in last_value    | op1, op2, [9]!     |
| 10    | mul(op1, op2)                    | Multiplies op1 and op2 then stores the value in last_value   | op1, op2, [10]!    |
| 11    | div(op1, op2)                    | Divides op1 and op2 then stores the value in last_value      | op1, op2, [11]!    |
| 12    | mod(op1, op2)                    | Modulus op1 and op2 then stores the value in last_value      | op1, op2, [12]!    |
| 13    | equals(op1, op2)                 | Checks if op1 was equal to op2 then stores the bool value in last_value | op1, op2, [13]!    |
| 14    | greater(op1, op2)                | Checks if op1 was greater than op2 then stores the bool value in last_value | op1, op2, [14]!    |
| 15    | less(op1, op2)                   | Checks if op1 was less than op2 then stores the bool value in last_value | op1, op2, [15]!    |
| 16    | negate(op1)                      | Negates op1 and stores it's value in last_value              | op1, [16]!         |
| 17    | and(op1, op2)                    | Ands op1 and op2 then stores that value in last_value        | op1, op2, [17]!    |
| 18    | or(op1, op2)                     | Ors op1 and op2 then stores that value in last_value         | op1, op2, [18]!    |
| 19    | index(list, index); index(index) | Stores the value of list[index] in last_value. If only index is provided, last_value[index] is stored in last_value | list, index, [19]! |

Developer Tip: If you get the syntax error "HOW DARE YOU", check the parameters you're are passing into the operation.

## Conditionals

Conditionals in Pyoem consist of three sections: a beginning line, internal logic, an ending line. The structure of the conditional is as follows:

| Section Type   | Definition                          | Description                                                | Example            |
| -------------- | ----------------------------------- | ---------------------------------------------------------- | ------------------ |
| Initial Line   | (^(?=.*[a-zA-Z].*)([a-zA-Z0-9]*)$)? | Checks if last_value is true                               | Start Conditional? |
| Internal Logic |                                     | If the conditional is true, this line(s) will be executed. |                    |
| Final Line     | (^(?=.*[a-zA-Z].*)([a-zA-Z0-9]*)$). | Concludes the conditional statement                        | End Conditional.   |

## For Loops (Foreach loops)

For loops in Pyoem are similar to conditionals in the sense of inital and final statements, however there is an additional line for dictating what is being looped over.

| Section Type   | Definition                            | Description                                                  | Example        |
| -------------- | ------------------------------------- | ------------------------------------------------------------ | -------------- |
| Initial Line   | (^(?=.*[a-zA-Z].*)([a-zA-Z0-9]*)$)... | Starts the loop section                                      | Start Loop...  |
| Loop Logic     | i, value, list                        | Defines the variables i and value, and provides the list to loop over | i, value, list |
| Internal Logic |                                       | If the loop logic is true, this line(s) will be executed.    |                |
| Final Line     | (^(?=.*[a-zA-Z].*)([a-zA-Z0-9]*)$).   | Ends the loop section                                        | End Loop.      |

## Function Calls

Pyoem supports the ability for developers to write their own functions and call them in other stanzas. Function declarations must be written before the main stanza that calls it. The name of the function corresponds to the values used from the parameters provided, if you have 3 parameters, the function name must have three words. You don't have to use all the words in the function name as parameters but your function name must have at least two words in it. The structure of a function is as follows: 

| Section Type   | Definition      | Description                                                  | Example       |
| -------------- | --------------- | ------------------------------------------------------------ | ------------- |
| Title          | ^(.*?[A-Z]){2,} | The title is made of at least 2 word that are all capitalized | FUNCTION CALL |
| Internal Logic |                 | If the function is called, this line(s) will be executed.    |               |

When calling a function the structure follows "parameter1, parameter2" (Function Call). The (Function Call) section references the function you made previously. The (Function Call) doesn't need to be capitalized here. The "parameter1, parameter2" indicates the list of parameters, for this example in the Function Call function, parameter1 maps to function and parameter 2 maps to call. 



