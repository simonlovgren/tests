#include <stdio.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
  uint8_t max = 255;

  for ( uint16_t i = 0; i <= max; ++i )
  {
    for ( uint16_t j = 0; j < max; ++j )
    {
      printf("%d", ((int8_t)(i)-(int8_t)(j)) >= 0);
    }
    printf("\n");
  }

  return 0;
}
