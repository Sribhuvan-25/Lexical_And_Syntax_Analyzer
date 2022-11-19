# Lexical Analyzer

### Rules
- Code starts with `start` and ends with `end`. Each lexeme is seperated by a space.

### Statements 
- Assignment
- Delaration
- Condition
- Loops

## TList
---

## Mathematical Operations
| Token Code       | Operation | Regex |
| ---------------- | --------- | ----- |
| ADD              | +         | +     |
| SUB              | -         | -     |
| MUL              | \*        | \*    |
| DIV              | /         | /     |
| OPENPARENTHES    | (         | )     |
| CLOSEPARENTHES   | )         | )     |


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
| Token Code | condition                                          | Regex | Size    |
| ---------- | -------------------------------------------------- | ----- | ------- |
| XS         | -128 <= num <= 127                                 | \d+   | 1 byte  |
| S          | -32768 <= num <= 32767                             | \d+   | 2 bytes |
| L          | -2147483648 <= num <= 2147483647                   | \d+   | 4 bytes |
| XL         | -9223372036854775808 <= num <= 9223372036854775808 | \d+   | 8 bytes |


## Keywords
| Token Code | Regex         |
| ---------- | ------------- |
| VAR        | [a-zA-Z]{6,8} |
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
- \-
- \+
- /
- \*
- (

## Production Rules

```txt
<Program> --> Begin <stmt_list> End
<stmt_list> --> {<stmt> `;`}
<stmt> --> <if_stmt> | <while_stmt> | <as_s>  | <declaration>
<if_stmt> --> cond <bool> `{` { <stmt> ';'} `}`
<while_stmt> --> repeat `{` <bool> { <stmt> ';' } `}`
<as_s> --> <var> = <expression>


<beq> --> <brel> { (`!=`|`==`) <brel> }
<brel> --> <expr> { (`<=`|`>=` | `<` | `>`) <expr> }
<expr> --> <term> { (`+`|`-`) <term> }
<term> --> <not> { (`*`|`\`|`%`) <bnot> }
<not> -> [!]<bfactor>
<factor> --> `id` | `int_lit`  | `(` <bexpr> `)`

E --> E + T             Expression + Term
E --> E - T             Expression - Term
E --> T                 Some expression can be a term
T --> T * F             Term * Factor
T --> T / F             Term / Factor
F --> -F                Unary Minus
F --> +F                Unary Plus
E --> a                 Factor can be a constant
E --> (E)               Factor can be an expression in parentheses
```

