from d1 import d1
from d2 import d2

def main():
    day("Calorelfic", lambda: d1("d1/input_1"))
    day("Rock Papelf Scissors", lambda: d2("d2/input_1"))

def day(banner, exec):
    print(f'{banner:=^60}')
    exec()

if __name__ == "__main__":
    main()
