#include <stdlib.h>
#include <stdio.h>

typedef int *nextptr;
typedef int *prevptr;

void nxt(nextptr n){
  puts("Next pointer");
}

void prv(prevptr n){
  puts("Prev pointer");
}

int main(int argc, char *argv[])
{

  nextptr n = malloc(sizeof(int));
  prevptr p = malloc(sizeof(int));
    
  prv(n);
  nxt(p);

  free(n);
  free(p);
  
  return 0;
}
