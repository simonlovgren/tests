#include <stdio.h>
#include "main.h"
#include "other.h"

#define MAIN_MSG() printf( "Main message: %d\n", __COUNTER__)


int main(int argc, char *argv[])
{
  printf("Main\n");
  MAIN_H_MSG();
  OTHER_H_MSG();
  MAIN_MSG();
  other();
  return 0;
}
