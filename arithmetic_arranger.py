def validate_elements(elements):
    # Only addition and subraction are allowed
    if elements[1] not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
    
    # Operands must be numbers
    try:
        int(elements[0])
        int(elements[2])
    except ValueError:
        return 'Error: Numbers must only contain digits.'
    
    # Each operand must have max 4 digits
    if len(elements[0]) > 4 or len(elements[2]) > 4:
        return 'Error: Numbers cannot be more than four digits.'

    return ''


def arithmetic_arranger(problems, show_result=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_line = []       # operand1
    bottom_line = []    # operator and operand2
    dash_line = []      # dashed line
    result_line = []    # result

    for problem in problems:
        elements = problem.split()  # [operand1, operator, opernad2]
        
        error = validate_elements(elements)
        if error:
            return error

        # Entire length of problem = longest operand + space + operator
        length = max(len(elements[0]), len(elements[2])) + 2

        top_line.append(f'{elements[0]:>{length}}')
        bottom_line.append(f'{elements[1]} {elements[2]:>{length-2}}')
        dash_line.append(f'{"-" * length}')
        if show_result:
            result_line.append(f'{str(eval(problem)):>{length}}')
    
    # four spaces between each problem
    separator = ' ' * 4

    # arrange output
    arranged_problems = separator.join(top_line) + '\n' + separator.join(bottom_line) + '\n' + separator.join(dash_line)
    if result_line:
        arranged_problems = arranged_problems + '\n' + separator.join(result_line)
    
    return arranged_problems