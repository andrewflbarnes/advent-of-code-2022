from d1 import d1
from d2 import d2
from d3 import d3
from d4 import d4
from d5 import d5
from d6 import d6
from d7 import d7
from d8 import d8
from d9 import d9
from d10 import d10
from d11 import d11
from d12 import d12
from d13 import d13

def main():
    day(1, "Calorelfic", lambda: d1("d1/input_1"))
    day(2, "Rock Papelf Scissors", lambda: d2("d2/input_1"))
    day(3, "Prielfitized Bags", lambda: d3("d3/input_1"))
    day(4, "Santa's little cleaners", lambda: d4("d4/input_1"))
    day(5, "Contain yourelf", lambda: d5("d5/input_1", 9))
    day(6, "Signelf processing", lambda: d6("d6/input_1"))
    day(7, "ELF file cleanup", lambda: d7("d7/input_1"))
    day(8, "Christmas tree house", lambda: d8("d8/input_1"))
    day(9, "Knotty or nice", lambda: d9("d9/input_1"))
    day(10, "Pixelfated sprites", lambda: d10("d10/input_1"))
    day(11, "Naughty Monkelfs", lambda: d11("d11/input_1"))
    day(12, "Helfy Hiking", lambda: d12("d12/input_1"))
    day(13, "Packelf Analysis", lambda: d13("d13/input_1"))

def day(num, banner, exec):
    print(f'Day {num:<3}{" " + banner + " ":=^60}')
    exec()

if __name__ == "__main__":
    main()
