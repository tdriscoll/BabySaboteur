


def make_pretty(input_str, max_width):
    input_str =  input_str
    pieces_of_string = input_str.split(" ")
    result = ""
    line_length = 0
    for piece in pieces_of_string:
        if not piece:
            continue
        line_length += len(piece) 
        if line_length  > max_width:
            result += "\n"
            line_length = len(piece)
        else:
            result += ' '
            line_length += 1
        result += piece
        
    return result.strip()