# RiscV ISA - RiscV ISA info and Tools

## Features

- "RiscV-Opcodes.xls" ISA Specifications
- "ParseExcel.py3" Tools for building *.h and *.cpp files
- "MakeDecode.py3" Tolls for building a *.v decoder file.

## RiscV-Opcodes.xls
The spreadsheet is used to specify the encoding of RV32 and RV64 instructions. For example the lw instruction is encoded as:

```
LW Example
--------------------------------------------
Bits        "iiiiiiiiiiiisssss010ddddd0000011"
Opcode      0x00002003
Mask        0x0000707f
Arch        rv32,rv64
Type        S-type
Asm         lw rd,rs,simm12
Function    rd <= mem32[rs1 + simm12]
```
The 'Bits' field is an encoded representation of the instruction bits. The encoded bits are:
```
	0/1	- actual 0 or 1 bit
	i	- immediate value
	d	- rd, destination register, 3 or 5 bits
	s	- rs1, source register 1, 3 or 5 bits 
	t	- rs2, source register 2, 3 or 5 bits
	a	- shift amount
	u	- 5 bit csr immediate
	x	- reserved
```
Note that there are cases where instruction encoding overlaps. In this case the more complete encoding should be described first. For example 'nop' is a special encoding of 'addi x0,x0,0'.

## ParseExcel.py3
The 'ParseExcel.py3' tools is used to parse the excel opcode table and extract c++ simulator *.cpp and *.h files. 

## MakeDecode.py3
The 'MakeDecode.py3' tools is used to parse the excel opcode table and extract a verilog decoder file. 

## Links
Some useful links ...

### Riscv.org:
https://riscv.org/technical/specifications/

### Unprivileged Spec:
https://github.com/riscv/riscv-isa-manual/releases/download/Ratified-IMAFDQC/riscv-spec-20191213.pdf

### Privileged Spec:
https://github.com/riscv/riscv-isa-manual/releases/download/Priv-v1.12/riscv-privileged-20211203.pdf


## License

    Copyright (c) 2022 Ron K. Irvine
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction for personal use only, including without
    limitation the rights to use, copy, modify, merge, publish and distribute
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The Software may not be used in connection with any commercial purposes, except as
    specifically approved by Ron K. Irvine or his representative. Unauthorized usage of
    the Software or any part of the Software is prohibited. Appropriate legal action
    will be taken by us for any illegal or unauthorized use of the Software.
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
