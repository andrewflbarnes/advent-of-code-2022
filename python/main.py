from d01 import d01
from d02 import d02
from d03 import d03
from d04 import d04
from d05 import d05
from d06 import d06
from d07 import d07
from d08 import d08
from d09 import d09
from d10 import d10
from d11 import d11
from d12 import d12
from d13 import d13
from d14 import d14

def main():
    day(1, "Calorelfic", lambda: d01("d01/input_1"))
    day(2, "Rock Papelf Scissors", lambda: d02("d02/input_1"))
    day(3, "Prielfitized Bags", lambda: d03("d03/input_1"))
    day(4, "Santa's little cleaners", lambda: d04("d04/input_1"))
    day(5, "Contain yourelf", lambda: d05("d05/input_1", 9))
    day(6, "Signelf processing", lambda: d06("d06/input_1"))
    day(7, "ELF file cleanup", lambda: d07("d07/input_1"))
    day(8, "Christmas tree house", lambda: d08("d08/input_1"))
    day(9, "Knotty or nice", lambda: d09("d09/input_1"))
    day(10, "Pixelfated sprites", lambda: d10("d10/input_1"))
    day(11, "Naughty Monkelfs", lambda: d11("d11/input_1"))
    day(12, "Helfy Hiking", lambda: d12("d12/input_1"))
    day(13, "Packelf Analysis", lambda: d13("d13/input_1"))
    day(14, "Cave spelflunking", lambda: d14("d14/input_1"))

def day(num, banner, exec):
    print(f'Day {num:<3}{" " + banner + " ":=^60}')
    exec()

if __name__ == "__main__":
    main()
