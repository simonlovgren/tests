#include "totp.h"

int main(int argc, char *argv[])
{
  puts("Sha1 hash test");

  if(argc >= 2) {
    printf("Hash of \"%s\"\n", argv[1]);
    puts(sha1(argv[1],strlen(argv[1])));
  } else{
    puts(sha1("",0));
  }
  return 0;
}
