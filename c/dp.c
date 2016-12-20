#include <stdio.h>
#include <stdlib.h>


struct stuff {
  int val;
  struct stuff *next;
};

int main(int argc, char *argv[])
{

  struct stuff *s1 = malloc(sizeof(struct stuff));
  struct stuff *s2 = malloc(sizeof(struct stuff));
  struct stuff *s3 = malloc(sizeof(struct stuff));

  struct stuff **dp = &(s1->next);
  
  s1->val = 33;
  s1->next = s2;
  s2->val = 42;
  s3->val = 53;

  
  printf("%d\n", s1->next->val);
  *dp = s3;
  printf("%d\n", s1->next->val);

  free(s1);
  free(s2);
  free(s3);
  
  return 0;
}
