# Lexical Analyzer

### Rules
- Code starts with `Start` and ends with `End`. Each lexeme is seperated by a space.

### Statements 
- Assignment
- Delaration
- Condition
- Loops

## Token List
---

## Mathematical Operations
| Token Code       | Operation | Regex |                                
| ---------------- | --------- | ----- |
| ADD              | +         | +     |
| SUB              | -         | -     |
| MUL              | \*        | \*    |
| MOD              | %         | %
| DIV              | /         | /     |
| OPEN             | (         | )     |
| CLOSE            | )         | )     |


## Comparisions
| Token Code | Operation | Regex |
| ---------- | --------- | ----- |
| LT         | <         | <     |
| GT         | >         | >     |
| LTE        | <=        | <=    |
| GTE        | >=        | >=    |
| EQ         | ==        | ==    |
| NE         | !=        | !=    |

## Integer Types
| Token Code | Size    |
| ---------- | ------- |
| XS         | 1 byte  |
| S          | 2 bytes |
| L          | 4 bytes |
| XL         | 8 bytes |


## Keywords
| Token Code | Regex         |
| ---------- | ------------- |
| VAR        | [a-zA-Z_]{6,8}|
| COND       | cond          |
| RERUN      | rerun         |
| START      | start         |
| END        | end           |

## Other
| Token Code       | Operation | Regex |
| ---------------- | --------- | ----- |
| ASSIGNMENT       | =         | =     |
| CODEBLOCKSTART   | {         | {     |
| CODEBLOCKEND     | }         | }     |

## Priority Order
- ()
- \*
- \-
- \+
- /
- %

## Production Rules

```txt
<Program> --> Start <stmt_list> End
<stmt_list> --> {<stmt> `;`}
<stmt> --> <if_stmt> | <while_stmt> | <as_s>  | <declaration>
<if_stmt> --> cond <bool> `{` { <stmt> ';'} `}`
<while_stmt> --> rerun `{` <bool> { <stmt> ';' } `}`
<as_s> --> <var> `=` <expression> `;`
<declaration> --> <datatype> <var> `;`

<datatype> --> (XS|S|L|XL)
<var> -->  [a-zA-Z_]{6,8}                       // Variable Naming restriction
<expression> --> <term> { (`*`|`\`|`%` ) <term> }
<term> --> <term> { (`+`|`-`) <term> }
<factor> --> [0-9]+ | <var>  | `(` <expression> `)`
<bool> --> <expression> (`<=`|`>=` | `<` | `>`) <expression>


E -> E + T          Expression + Term
E -> E - T          Expression - Term
E -> T              Some expression can be a term
T -> T * F          Term * Factor
T -> T / F          Term / Factor
T -> F              Some Terms can be Factors
F -> -F             Unary Minus
F -> +F             Unary Plus
F ->( E )           Factor can be an Expression in parentheses
F -> c              Factor can be a constant
```
## (C) Is it LL Grammar ?
The code works on the principle of LR grammar and wouldn't have pairwise disjointness. It fillows push down or top down automata

## (D) Is the Grammar Ambiguous ?
The LR table would have highlighted the ambiguous parts in red which is in the action block. The following image shows that there isn't any ambiguity.

## (G) Test Files
### Failing Test cases
```txt
Start
    XL var1A;
    var1A = 5 - (2 * 5);

    Xs varOne;
    varOne = 1;

    cnd ( varOne < = 1) {
        varOne = 10;
    }

    XL varTw;
    varTwo = varO+ 5;
End
```
#### Lexical Errors in the code:
- Cnd should have been Cond.
- var1A is not correct naming convention as it can't have numbers in it.
- varTw should have been varTwo
- Xs should have been XS
- varO should have been varOne

```txt
Start

  XL varA;
  varA = 1-5 + 2;

  cond (varA > = 4 {
    varA = 20;

    cond (varA != 2) {
      varA = varA % 2;

    XL varB;
    varB = 1 - 7 * ( 1 / 2 ;
  }

End
```
#### Syntax errors in the code:
- (1 / 2 :  is missing closing parentheses `)`
- (varA > = 4 : should end with closing parentheses `)'
- (varA > = 4 : there is no space in between the two '>=`.
- cond statement is missing a closing parentheses `}`.
- 1-5 shoud have space between each lexeme `1 - 5`.


### Working test cases
```txt
Start

  S varOne;
  varOne = 1;

  XL varTwo;
  varTwo = 1 + 1 + (2 + (100 * 2)) * varOne;

  cond (varOne == varTwo) {
    cond (varOne <= varTwo) {
      varOne = varTwo * 2;
    }
  }

  XS varThree;
  varThree = 0;

  rerun (varThree <= 2) {
    varThree = varThree + 4;

    cond (varThree == 3) {
      varThree = varThree * 2;
    }
  }

End
```
```txt
Start 

    XL varOne;
    varOne = 2 * 4 - 1;

    XS varTwo;
    varTwo = 4;

    L var_a;

    cond (varTwo < varOne){
        var_a = 1;
    }
End
```

## (H) LR(1) Grammar and parse tree

### LR(1) Grammar
![Grammar table](https://raw.githubusercontent.com/Sribhuvan-25/Lexical_And_Syntax_Analyzer/main/Images/Picture1.png)

### LR(1) Parse Table
![Grammar table](https://raw.githubusercontent.com/Sribhuvan-25/Lexical_And_Syntax_Analyzer/main/Images/ParseTable.png)

### Fail 1
![Grammar table](https://raw.githubusercontent.com/Sribhuvan-25/Lexical_And_Syntax_Analyzer/main/Images/Fail1.png)

### Pass 1
![Grammar table](https://raw.githubusercontent.com/Sribhuvan-25/Lexical_And_Syntax_Analyzer/main/Images/Pass1.png)

### Fail 2
![Grammar table](https://raw.githubusercontent.com/Sribhuvan-25/Lexical_And_Syntax_Analyzer/main/Images/Fail2.png)

### Pass 2
![Grammar table](https://raw.githubusercontent.com/Sribhuvan-25/Lexical_And_Syntax_Analyzer/main/Images/Pass2.png)










