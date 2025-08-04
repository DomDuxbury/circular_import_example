from module_2 import hello

def from_module():
    print("from module")

def hello_from_module():
    hello()
    from_module()
