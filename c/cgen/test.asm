	.globl main
	.text
main:
	addi $a0 $zero 100
	sw $a0 0($sp)
	addi $sp $sp -4
	addi $a0 $zero 123
	lw $t1 4($sp)
	addi $sp $sp 4
	sub $a0 $a0 $t1
	sw $a0 0($sp)
	addi $sp $sp -4
	addi $a0 $zero 456
	lw $t1 4($sp)
	addi $sp $sp 4
	add $a0 $a0 $t1
li $v0, 10
syscall
