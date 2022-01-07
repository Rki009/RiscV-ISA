

def main():
	file_name = "RiscV-Opcodes.xls"

	from pandas import read_excel
	# find your sheet name at the bottom left of your excel file and assign 
	df = read_excel(file_name, sheet_name = 'Sheet1')

	# print(df.head()) # shows headers with top 5 rows
	# print("Info:", df.info());
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
	doOpTable(df, arch)
	doOpVliwH(df, arch)
	doOpVliwCpp(df, arch)

	# rv64
	arch = "rv64"
	doOpTable(df, arch)
	doOpVliwH(df, arch)
	doOpVliwCpp(df, arch)
	return


def doOpTable(df, arch):
	# Output *.cpp data table
	fname = "OpTable.h"
	print("Make:", fname) 
	f = open(fname, "w")
	f.write("// RiscV Opcode Table Data\n")
	f.write("class Optable {\n")
	f.write("public:\n")
	f.write("	const char*		bitText;\n")
	f.write("	uint32_t		code;\n")
	f.write("	uint32_t		mask;\n")
	f.write("	uint32_t		vliw;\n")
	f.write("	const char*		asmText;\n")
	f.write("};\n")
	f.write("\n")
	f.close

	fname = "OpTable_" + arch + ".cpp"
	print("Make:", fname) 
	f = open(fname, "w")
	f.write("// RiscV Opcode Table Data\n")
	f.write("Optable optable[] = {\n")
	i = 0
	while i < len(df):
		if arch in str(df.iloc[i][3]):
			# print(str(df.iloc[i][3]))
			data = '\t{ "' + str(df.iloc[i][0]) + '", '	# Bits
			data += df.iloc[i][1] + ', '				# Opcode
			data += df.iloc[i][2] + ', '				# Mask
			# data += '"' + str(df.iloc[i][3]) + '", '	# Arch
			# data += '"' + str(df.iloc[i][4]) + '", '	# Type
	
			text = str(df.iloc[i][5])
			tag = text.split()
			text = tag[0]
			text = text.replace('.', '_')
			data += "%-16.16s "%('VLIW_' + text.upper() + ',')

			data += '"' + str(df.iloc[i][5]) + '" },\n'	# Asm
			# data += '"' + str(df.iloc[i][6]) + '", '	# Function
			# data += '"' + str(df.iloc[i][7]) + '" },\n'	# Description
			f.write(data)
		i += 1
	f.write("\t{ NULL, 0, 0, 0, NULL }\n")
	f.write("};\n")
	f.close()
	return


# output Vliw Header file
def doOpVliwH(df, arch):
	fname = "VliwTable_" + arch + ".h"
	print("Make:", fname) 
	f = open(fname, "w")
	f.write("#define VLIW_NONE             0x00\n");
	i = 0
	n = 1	# 0 == VLIW_NONE
	while i < len(df):
		if arch in str(df.iloc[i][3]):
			text = str(df.iloc[i][5])
			tag = text.split()
			text = tag[0]
			text = text.replace('.', '_')
			index = '0x%02x'%int(n)
			n += 1
			text = '#define ' + 'VLIW_' + '%-16.16s '%text.upper() + index + '\n' 
			f.write(text)
		i += 1
	f.write("#define VLIW_SIZE             " + '0x%02x'%int(n) + '\n');
	f.close()
	return

# output Vliw Table
def doOpVliwCpp(df, arch):
	fname = "VliwTable_" + arch + ".cpp"
	print("Make:", fname) 
	f = open(fname, "w")
	f.write("const char* VliwName[" + '%d'%int(len(df)) + "] = {\n");
	f.write('\t"VLIW_NONE",\n')
	i = 0
	n = 0
	while i < len(df):
		if arch in str(df.iloc[i][3]):
			text = str(df.iloc[i][5])
			tag = text.split()
			text = tag[0]
			text = text.replace('.', '_')
			index = '0x%02x'%int(n)
			n += 1
			text = '\t"VLIW_' + '%s",\n'%text.upper() 
			f.write(text)
		i += 1
	# f.write("\tNULL\n");
	f.write("};\n");
	f.close()
	return


if __name__ == "__main__":
	main()
	quit()



