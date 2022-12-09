from d1 import d1
from d2 import d2
from d3 import d3
from d4 import d4
from d5 import d5
from d6 import d6
from d7 import d7
from d8 import d8
from d9 import d9

def main():
    day("Calorelfic", lambda: d1("d1/input_1"))
    day("Rock Papelf Scissors", lambda: d2("d2/input_1"))
    day("Prielfitized Bags", lambda: d3("d3/input_1"))
    day("Santa's little cleaners", lambda: d4("d4/input_1"))
    day("Contain yourelf", lambda: d5("d5/input_1", 9))
    day("Signelf processing", lambda: d6("d6/input_1"))
    day("ELF file cleanup", lambda: d7("d7/input_1"))
    day("Christmas tree house", lambda: d8("d8/input_1"))
    day("Knotty or nice", lambda: d9("d9/input_1"))

def day(banner, exec):
    print(f'{" " + banner + " ":=^60}')
    exec()

if __name__ == "__main__":
    main()
