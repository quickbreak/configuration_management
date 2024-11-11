import json


def translate_value(value, space):
    if type(value) == type(1):
        return value
    elif type(value) == type("1"):
        return f"@\"{value}\""
    elif type(value) == type([1]):
        return "({ " + str(value)[1:-1] + " })"
    else:
        return translate_dict(value, space + "   ")


def calc_expressions(expressions, constants, space):
    result = ""
    for expr in expressions:
        expr_copy = expr
        expr = expr.replace('?', '').replace('[', '').replace(']', '').split()
        if len(expr) == 3:
            operation = expr[2]
            operand_1 = constants[expr[0]]
            operand_2 = constants[expr[1]]
            if operation == 'add':
                result += (space + "@\"result for " + expr_copy +
                           "\" = " + str(int(operand_1) + int(operand_2))) + '\n'
            elif operation == 'concatenate':
                result += (space + "@\"result for " + expr_copy +
                           "\" = @\"" + operand_1 + operand_2 + "\"") + '\n'
            elif operation == 'max':
                result += (space + "@\"result for " + expr_copy +
                           "\" = " + str(max(int(operand_1), int(operand_2)))) + '\n'
            else:
                print(f'wrong expression: {expr}')
                exit(0)
        else:  # len(expr) == 2
            print(f'wrong expression: {expr}')
            exit(0)
    return result


def translate_dict(dictionary, space):
    result = "dict(" + '\n'
    content = dictionary
    constants = {}
    expressions = []
    for key in content:
        value = content[key]
        if 'constant' in key:
            constants[key] = value
        elif 'expression' in key:
            expressions.append(value)

        if 'constant' in key:
            result += (space + f'global @"{key}" = {translate_value(value, space)}') + '\n'
        else:
            result += (space + f'@"{key}" = {translate_value(value, space)}') + '\n'

    result += calc_expressions(expressions, constants, space)
    result += (space[:-3] + ")")
    return result


def translate(from_path, to_path):
    with open(from_path, 'r', encoding='utf-8') as content_file:
        content = json.load(content_file)

    space = "   "
    ans = (translate_dict(content, space))
    # print(ans)
    with open(to_path, 'w') as output:
        output.write(ans)
    return ans
