This is a simple CKY parser for natural language processing. The program was tested under Ubuntu 18.04 with python3.6
interpreter. To run the program, type "python3 CKY_parser.py". The program will ask the user to input the path of a
file containing the grammar. The grammar must be in CNF form. After reading the grammar file, the program will ask for
a sentence whose grammar will be validated. If the sentence has valid grammar, all valid parses will be outputted in
bracketed notation. If not, the program will output "NO VALID PARSES". At the end of each sentence validation, the user
can quit the program by typing in "quit". Typing other strings will be considered as continuing the program.