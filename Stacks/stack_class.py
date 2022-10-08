
stack = []
def push( element):
    stack.append(element)
def isEmpty():
    if len(stack) == 0:
        return True
def pop():
    if isEmpty():
        print("No more elements")
    else:
        stack.pop()

def show():
    for i in stack:
        print("|", i ,"|" )
    print("- - -")

if __name__ == "__main__":
    push(10)
    push(20)
    push(30)
    
    pop()
    pop()
    pop()
    pop()
    pop()
    pop()
    show()