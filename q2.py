def align_brackets_with_marks(strings):
    aligned_outputs = []
    for string in strings:
       
        alignment_line = [' ' for _ in range(len(string))]
        open_brackets_stack = []
        
        for i, char in enumerate(string):
            if char == '(':
                open_brackets_stack.append(i) 
            elif char == ')':
                if open_brackets_stack:
                    open_brackets_stack.pop()  
                else:
                    alignment_line[i] = '?'  
        
        for index in open_brackets_stack:
            alignment_line[index] = 'x'
        
      
        combined_string = string + '\n' + ''.join(alignment_line)
        aligned_outputs.append(combined_string)
    
    return '\n\n'.join(aligned_outputs)

formatted_output_correct = align_brackets_with_marks(test_inputs)
print(formatted_output_correct)
