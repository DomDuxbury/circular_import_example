def main():
    hello()
    print("from main")
    hello_from_module()

def hello():
    print("hello")

def from_module():
    print("from module")

def hello_from_module():
    hello()
    from_module()

if __name__ == "__main__":
    main()
