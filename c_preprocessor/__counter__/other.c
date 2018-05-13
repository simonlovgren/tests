#include <stdio.h>
#include "other.h"

#define OTHER_MSG() printf( "Other message: %d\n", __COUNTER__)

void other()
{
  printf( "other\n" );
  OTHER_H_MSG();
  OTHER_MSG();
}
