"""
Validate parenthesis
--------------------
Make sure every input string provided has valid parenthesis.
If it does, return True, else False.
"""


def validate_parenthesis(input_string):
    if not input_string:
        return True
    open_brackets = {
        '{': True,
        '(': True,
        '[': True,
    }
    close_brackets = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    stack_brackets = []
    for char in input_string:
        if char in open_brackets:
            stack_brackets.append(char)
        if char in close_brackets:
            matching_open = stack_brackets.pop()
            if close_brackets[char] != matching_open:
                return False
    if stack_brackets:
        return False
    return True

def main():
    assert True == validate_parenthesis("(abc[{}])")
    assert False == validate_parenthesis("(abc}])")
    assert False == validate_parenthesis("(abc[{")


if __name__ == '__main__':
    main()
