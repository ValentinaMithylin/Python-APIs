# def greeting():
#     return "Hello, world!"

# def sum_func():
#     num1 = int(request.vars.num1)
#     num2 = float(request.vars.num2)
#     return response.json({'total': num1+num2})

def one_str():
    string = request.vars.str
    return string

def test_func():
    string1 = request.vars.str1
    string2 = request.vars.str2
    return response.json({'message': string1+string2})