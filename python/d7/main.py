import re

def main():
    d7('input_test')
    d7('input_1')

pat_cd = re.compile(r"\$ cd (.+)")
pat_file = re.compile(r"(\d+) (.+)")

def d7(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    dir = []
    curr_folder = {'name': "/", 'files': [], 'folders': []}

    for line in lines:
        if (match := pat_cd.match(line)):
            match match.group(1):
                case "/":
                    pass
                case "..":
                    curr_folder = dir.pop()
                case sub_folder:
                    dir.append(curr_folder)
                    new_folder = {'name': sub_folder, 'files': [], 'folders': []}
                    curr_folder['folders'].append(new_folder)
                    curr_folder = new_folder
        elif (match := pat_file.match(line)):
            curr_folder['files'].append((match.group(2), match.group(1)))
        else:
            pass # ignore dir and ls commands

    fs = dir[0]
    # print_fs(fs)

    # part 1
    small_folders = [folder_size(f) for f in visit_folder(fs, lambda folder : folder_size(folder) <= 100_000)]
    print(sum(small_folders))

    # part 2
    req_del_size = 30_000_000 - 70_000_000 + folder_size(fs)
    if (req_del_size > 0):
        del_sizes = [folder_size(f) for f in visit_folder(fs, lambda folder : folder_size(folder) >= req_del_size)]
        del_sizes.sort()
        print(del_sizes[0])

def folder_size(folder):
    return sum([int(file[1]) for file in folder['files']]) + sum([folder_size(sub_folder) for sub_folder in folder['folders']])

def visit_folder(folder, condition, acc = None):
    if acc is None:
        acc = []
    if (condition(folder)):
        acc.append(folder)
    for sub_folder in folder['folders']:
        visit_folder(sub_folder, condition, acc)
    return acc

def print_fs(folder, prep = ""):
    print(f'{prep}{folder["name"]}/')
    for file in folder['files']:
        print(f'{prep}- {file[0]}: {file[1]}')
    for sub_folder in folder['folders']:
        print_fs(sub_folder, prep + "  ")

if __name__ == "__main__":
    main()