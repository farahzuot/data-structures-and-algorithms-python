def multi_bracket_validation(input):
    stack = [] 
    for i in input: 
        if i in ["(", "{", "["]: 
            stack.append(i) 
        else: 
            if not stack: 
                return False
            current_i = stack.pop() 
            if current_i == '(': 
                if i != ")": 
                    return False
            if current_i == '{': 
                if i != "}": 
                    return False
            if current_i == '[': 
                if i != "]": 
                    return False
    if stack: 
        return False
    return True
  


if __name__ == "__main__":
    print(multi_bracket_validation('[][]'))
    print(multi_bracket_validation('[][{]'))
    print(multi_bracket_validation('[[{}]]'))