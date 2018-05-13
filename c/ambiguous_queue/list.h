#include <stdlib.h>

#ifndef LIST
#define LIST

typedef struct list_s list;

list *list_new();

list *list_free(list *l);

void list_prepnd(list *l, void *data);

void list_append(list *l, void *data);

void *list_pop(list *l, size_t index);

#endif
