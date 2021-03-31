// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
/**	
 *		Mov R0, #4;
 *		Mov R1, #4;
 *
 *		CMP R0, #0;
 * 		BGE comp1
 *
 *comp1 CMP R1, #0;
 *		BGE multicomp;
 *
 *multicomp		Multi R3, R0, R1;		
 *				CMP R3, 32768;
 *				BLT movR2
 *	
 *movR2	Mov R2, R3;
 */

 @R2
 M=0

