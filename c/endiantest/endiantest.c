#include <stdio.h>

int main()
{
  unsigned int x = 1;
  if(((char *)&x)[0] == 0) {
    puts("BIG ENDIAN");
  } else {
    puts("LITTLE ENDIAN");
  }
  return 0;
}
