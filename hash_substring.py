# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function

    data = input()
    if data[0]=="I":
        patern=input()
        text = input()
    elif data[0]=="F":
        filename = "tests/"
        filename = filename + input()
        if filename[-1] == 'a':
            return
        with open(filename, 'r') as file:
            data = file.read()
            lines = data.split('\n')
            patern = lines[0]
            text = lines[1]
    return (patern.rstrip(), text.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(patern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    patern_l = len(patern)
    text_l = len(text)

    patern_h = hash(patern)
    text_h = hash(text[:patern_l])
    output = []
    for i in range(text_l-patern_l+1):
        if patern_h == text_h and patern == text[i:i+patern_l]:
            output.append(i)
        text_h = hash(text[i+1:i+patern_l+1])
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

