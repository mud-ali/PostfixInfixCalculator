def isnum(num):
    if num.isnumeric(): return True
    try:
        float(num)
        return True
    except ValueError:
        return False

def parse(x, symbol, y):
    a = float(x)
    b = float(y)
    match symbol:
        case "+":
            return str(a+b)
        case "-":
            return str(a-b)
        case "*":
            return str(a*b)
        case "/":
            return str(a/b)
        case "^":
            return str(a**b)
    return None

def inf(string):
    return eval(string)

def pref(string):
    eq = string.split()
    if len(eq) == 1:
        return eq[0]

    for index in range(len(eq)):
        symbol = eq[index]
        prev = None if index == 0 else eq[index-1]
        nxt = None if index == len(eq)-1 else eq[index+1] 

        if isnum(symbol) and nxt is not None \
            and isnum(nxt)\
            and prev is not None\
            and prev in "+-*/^":
            val = parse(symbol, prev, nxt)
            eq[index] = val
            eq[index-1] = ""
            eq[index+1] = ""
            index -= 2
            return pref(" ".join(eq))

def postf(string):
    eq = string.split()
    if len(eq) == 1:
        print("ans: ",end='')
        return eq[0]

    for index in range(len(eq)):
        symbol = eq[index]
        prev = None if index == 0 else eq[index-1]
        nxt = None if index == len(eq)-1 else eq[index+1] 

        if isnum(symbol) and prev is not None \
            and isnum(prev)\
            and nxt is not None\
            and nxt in "+-*/^":
            val = parse(prev, nxt, symbol)
            eq[index] = val
            eq[index-1] = ""
            eq[index+1] = ""
            index -= 2
            return postf(" ".join(eq))

def main():
    with open('input.txt', 'r') as in_file:
        for line in in_file.read().splitlines():
            if line.startswith("in:"):
                print(inf(line.replace("in:",'')))
            elif line.startswith("pre:"):
                print(pref(line.replace("pre:",'')))
            elif line.startswith("post:"):
                print(postf(line.replace("post:",'')))

if __name__ == '__main__':
    main()