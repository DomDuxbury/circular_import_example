from module_1.module_1 import hello_from_module

def main():
    hello()
    print("from main")
    hello_from_module()

def hello():
    print("hello")

if __name__ == "__main__":
    main()
