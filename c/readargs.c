#include <stdio.h>
#include <string.h>



int main(int argc, char *argv[])
{

  for(int i = 0; i < argc; ++i) {
    printf("%d  %s", i, argv[i]);
    if(strlen(argv[i]) == 2 && strncmp(argv[i], "--", 2) == 0) {
      printf(" (2 chars, -- delim)");
    }
    putchar('\n');
  }
  
  return 0;
}
