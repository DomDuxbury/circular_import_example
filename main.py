from module_1 import hello_from_module
from module_2 import hello

def main():
    hello()
    print("from main")
    hello_from_module()

if __name__ == "__main__":
    main()
