import re

def main():
	file_name = "RiscV-Opcodes.xls"

	from pandas import read_excel
	# find your sheet name at the bottom left of your excel file and assign 
	df = read_excel(file_name, sheet_name = 'Sheet1')

	# print(df.head()) # shows headers with top 5 rows
	print("Info:", df.info());
	print("Shape:", df.shape);
	# print("Rows:", len(df));
	# print("Cols:", len(df.columns));

	# print("22:", df.iloc[22])
	# print("37:", df.iloc[37]['Opcode'])
	# print("39:", df.iloc[39][2])

	# Fix Nan for empty string :(
	i = 1
	while i < len(df):
		j = 0
		while j < len(df.columns):
			if str(df.iloc[i][j]) == 'nan':
				df.iloc[i][j] = ''
			j += 1
		i += 1
	
	# rv32
	arch = "rv32"
	dodecode(df, arch)
	return


def dodecode(df, select):
	# Output *.cpp data table
	fname = "decode32Table.v"
	print("Make:", fname) 
	f = open(fname, "w")
	f.write("// RiscV32 Decode Table\n")
	f.write("\tcasez (insn)\n")
	i = 0
	while i < len(df):
		bits = str(df.iloc[i][0])
		opcode = str(df.iloc[i][1])
		mask = str(df.iloc[i][2])
		arch = str(df.iloc[i][3])
		type = str(df.iloc[i][4])
		asm = str(df.iloc[i][5])
		func = str(df.iloc[i][6])
		desc = str(df.iloc[i][7])
		if select in arch and len(bits) == 32:
			text = asm
			tag = text.split()
			text = tag[0]
			text = text.replace('.', '_')
			text = "\t// " + text.upper() + " - " + asm + "\n"
			f.write(text)
			data = bits
			data = re.sub(r"[a-zA-Z]", "?", data)
			data = "\t32'b" + data + ": begin\n"	# Bits
			f.write(data)
			f.write("\tend\n")
			f.write("\n")
		i += 1
	f.write("\tdefault: begin\n")
	f.write("\tend\n")
	f.write("\tendcase\n")
	f.close()
	return



if __name__ == "__main__":
	main()
	quit()



