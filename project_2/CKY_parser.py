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
            left, right = line.split(" --> ")
            key = right.replace(" ", "$")
            if key not in grammar:
                grammar.update({key: [left]})
            else:
                grammar[key].append(left)


def cky_parse(words, grammar):
    table = []
    for i in range(len(words), 0, -1):
        table.append([[]] * i)
    for j in range(1, len(words) + 1, 1):
        word = words[j-1]
        if word in grammar:
            for rule in grammar[word]:
                cell = TableCell(rule, cell_type=0, comp1=(word, 0, 0), comp2=(None, 0, 0))
                table[j-1][j].append(cell)
        for i in range(j-2, -1, -1):
            for k in range(i+1, j, 1):
                pass
