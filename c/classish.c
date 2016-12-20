#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct mclass MyClass;
struct mclass{
  void (*setName)(MyClass *, char *);
  char *(*getName)(MyClass *);
  void (*destroy)(MyClass *);
  char *name;
};

void destroy(MyClass *self){
  free(self->name);
  free(self);
}

void setName(MyClass *self, char *name) {
  free(self->name);
  self->name = strdup(name);
}

char* getName(MyClass *self) {
  return self->name;
}

MyClass *newMyClass() {
  MyClass *m = malloc(sizeof(MyClass));
  m->getName = getName;
  m->setName = setName;
  m->destroy = destroy;
  m->name = NULL;
  return m;
}


int main(int argc, char *argv[])
{
  MyClass *mc = newMyClass();
  mc->setName(mc, "Hamtaro");
  puts(mc->getName(mc));
  mc->setName(mc, "Sally");
  puts(mc->getName(mc));
  mc->destroy(mc);
  
  return 0;
}
