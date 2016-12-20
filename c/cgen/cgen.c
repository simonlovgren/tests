#include <stdlib.h>
#include <stdio.h>

/* Enumerated token types */
typedef enum e_token_type {
  INT,
  ADD,
  SUB,
  MAIN
} token_type;

/* Struct for representing a token */
typedef struct s_token token;
struct s_token {
  token_type type;
  void *value;
};

/* Struct for storing expression/token tree */
typedef struct s_expr expr;
struct s_expr{
  token token;
  unsigned int n_subexpr;
  expr **subexpr;
};

/**
 * cgen generate language from expression
 */
void cgen(expr *e)
{
  switch (e->token.type)
    {
    case INT:
      printf("\taddi $a0 $zero %d\n", *((int *)e->token.value));
      break;

    case ADD:
      cgen(e->subexpr[0]); /* Evaluate first subexpression */
      puts("\tsw $a0 0($sp)"); /* Store result to stack*/
      puts("\taddi $sp $sp -4"); /* Adjust stack pointer*/
      cgen(e->subexpr[1]); /* Evaluate second subexpression */
      puts("\tlw $t1 4($sp)"); /* Load first result from stack to $t1 */
      puts("\taddi $sp $sp 4"); /* Restore stack pointer*/
      puts("\tadd $a0 $a0 $t1"); /* Calculate addition of results*/      
      break;

    case SUB:
      cgen(e->subexpr[0]); /* Evaluate first subexpression */
      puts("\tsw $a0 0($sp)"); /* Store result to stack*/
      puts("\taddi $sp $sp -4"); /* Adjust stack pointer*/
      cgen(e->subexpr[1]); /* Evaluate second subexpression */
      puts("\tlw $t1 4($sp)"); /* Load first result from stack to $t1 */
      puts("\taddi $sp $sp 4"); /* Restore stack pointer*/
      puts("\tsub $a0 $a0 $t1"); /* Calculate subtraction of results*/      
      break;
      
    case MAIN:
      puts("\t.globl main");
      puts("\t.text");
      puts("main:");
      cgen(e->subexpr[0]);
      puts("li $v0, 10");
      puts("syscall");
      break;
    default:
      /* Something is not right... */
      break;
    }
}

int main(int argc, char *argv[])
{
  int int0_val = 100;
  int int1_val = 123;
  int int2_val = 456;
  expr int0 = {(token){INT,&int0_val},0,NULL};
  expr int1 = {(token){INT,&int1_val},0,NULL};
  expr int2 = {(token){INT,&int2_val},0,NULL};

  expr *sub1[2];
  sub1[0] = &int0;
  sub1[1] = &int1;
  expr sub = {(token){SUB,NULL},2,sub1};
  
  expr *sub2[2];
  sub2[0] = &sub;
  sub2[1] = &int2;
  expr add = {(token){ADD,NULL},2,sub2};

  expr *pgm[1];
  pgm[0] = &add;
  expr program = {(token){MAIN,NULL},1,pgm};
  
  cgen(&program);
  return 0;
}
