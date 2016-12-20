#include <stdio.h>
#include <stdint.h>

void badfunction() {
  puts("maliciously delicious!");
}

void overflower(size_t *c, int start){
    for(int i = 7; i > 0; --i) {
    c[start - i] = badfunction;
  }
  puts("done");
}

void overflowme(size_t *c, int start){
  overflower(c,start);
}

int main(int argc, char *argv[])
{
  uint8_t a = 11;
  uint8_t b = 22;

  size_t c[10];

  printf("Stack location (a):     %zx\n", (size_t)&a);
  printf("Stack location (b):     %zx\n", (size_t)&b);
  printf("Stack location (c[0]):  %zx\n", (size_t)&c[0]);
  printf("Stack location (c[10]): %zx\n", (size_t)&c[10]);
  printf("Stack location (c[-1]): %zx\n", ((size_t)&c[-25]));
  printf("before (a):    %hhx\n", a);
  overflowme(c,0);
  printf("after (a):     %hhx\n", a);
  return 0;
}
