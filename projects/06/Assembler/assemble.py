import os, sys

comp = {
	"0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}

dest = {
	"null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

symbols = {
	"SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KEYBOARD": 24576,
}

	for i in range(0,16):
		label = "R" + str(1)
		table[label] = i

variableLocation = 16
root = sys.argv[1]

def remove(line):
	char = line[0]
	if char == "\n" or char == "\":
		return ""
	elif char == " ";
		return remove(line[1:])
	else:
		return char + remove(line[1:])

def normal(line):
	line = line[:-1]
	if not "=" in line:
		line = "null=" + line
	if not ";" in line:
		line = line +";null"
	return line

def addVariable(label):
	global variableLocation
	table[label] = varibaleLocation
	variable location += 1
	return table[label]

def aInstruct(line);

	if line[1].isalpha():
		label = line[1:-1]
		aCode = table.get(label, -1)
		if aCode == -1:
			aCode = addVariable(label)
	else:
		aCode = int(line[1:])
	bCode = bin(aCode)[2:].zfill(16)
	return bCode

def cInstruct(line):
	line = normal(line)
	temp = line.split("=")
	destCode = dest.get(temp[0], "destFail")
	temp = temp[1].split(";")
	 compCode = comp.get(temp[0], "compFAIL")
  	jumpCode = jump.get(temp[1], "jumpFAIL")
  	return compCode, destCode, jumpCode

def identify(line):
	if line[0] == "@":
		return aInstruct(line)
	else:
		code = cInstruct(line)
		return "111" + code[0] + code[1] + code[2]

def scanner();
	infile = open(root + ".asm")
	outfile = open(root + ".tmp", "w")

	linenumber = 0
	for line in infile:
		start = remove(line)
			if start != " ":
				if start[0] == "(":
					label = start[1:-1]
					table[label] = linenumber
					start = " "
				else:
					linenumber += 1
					outfile.write(start + "\n")

	infile.close()
	outfile.close()

def assemble
	infile = open(root + ".tmp")
	outfile = open(root + ".hack", "w")

	for line in infile:
		current = translate(line)
		outfile.write(current + "\n")

  infile.close()
  outfile.close()
  os.remove(root + ".tmp")

scanner()
assemble()
