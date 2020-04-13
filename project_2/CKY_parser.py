import re


class TableCell:
    def __init__(self, prod, cell_type, comp1, comp2):
        self.prod = prod
        self.cell_type = cell_type  # 0 stands for a terminal symbol, 1 stands for non-terminal symbol
        self.comp1 = comp1
        self.comp2 = comp2


def load_cnf(file_path):
    grammar = {}
    with open(file_path) as f:
        for line in f:
            left, right = line.replace("\n", "").split(" --> ")
            key = right.replace(" ", "$")
            if key not in grammar:
                grammar.update({key: [left]})
            else:
                grammar[key].append(left)
    return grammar


def cky_parse(words, grammar):
    table = []
    words_len = len(words)
    for i in range(words_len, 0, -1):
        table.append([[] for x in range(words_len + 1)])
    for j in range(1, words_len + 1, 1):
        word = words[j-1]
        if word in grammar:
            for rule in grammar[word]:
                cell = TableCell(prod=rule, cell_type=0, comp1=(word, 0, 0), comp2=(None, 0, 0))
                table[j-1][j].append(cell)
        else:
            return None
        for i in range(j-2, -1, -1):
            for k in range(i+1, j, 1):
                for cell_b in table[i][k]:
                    for cell_c in table[k][j]:
                        constituent = cell_b.prod + "$" + cell_c.prod
                        if constituent in grammar:
                            for prod in grammar[constituent]:
                                cell = TableCell(prod=prod, cell_type=1, comp1=(cell_b.prod, cell_b), comp2=(cell_c.prod, cell_c))
                                table[i][j].append(cell)
    return table


def display_cell(table, cell):
    if cell.cell_type == 0:
        print("[" + cell.prod + " " + cell.comp1[0] + "]", end="")
    else:
        print("[" + cell.prod + " ", end="")
        display_cell(table, cell.comp1[1])
        display_cell(table, cell.comp2[1])
        print("]", end="")


def display_parse_tree(table):
    cells = table[0][-1]
    if len(cells) == 0:
        print("NO VALID PARSES")
    for i in range(len(cells)):
        print("Parse " + str(i+1) + ":", end="")
        display_cell(table, cells[i])
        print("")


if __name__ == "__main__":
    cnf_path = input("Please enter the path to the CNF grammar file: ")
    cnf_grammar = load_cnf(cnf_path)
    while True:
        raw_sentence = input("Please enter a sentence that you want to validate: ")
        sentence = re.sub(r'[^a-zA-Z0-9 ]+', '', raw_sentence).lower()
        words_input = sentence.split(" ")
        table_result = cky_parse(words_input, cnf_grammar)
        if table_result is None:
            print("NO VALID PARSES")
        elif len(table_result[0][len(words_input)]) == 0:
            print("NO VALID PARSES")
        else:
            display_parse_tree(table_result)
        user_exit = input("Type \"quit\" to exit the program?").lower()
        if user_exit == "quit":
            break
