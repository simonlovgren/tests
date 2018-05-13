#include "list.h"

typedef struct node_s node;
struct node_s {
  void *data;
  node *prev;
  node *next;
};

struct list_s {
  size_t size;
  node *head;
  node *tail;
};

list *list_new() {
  return  calloc(1,sizeof(list));
}

list *list_free(list *l) {
  node *cursor = l->first;
  while(cursor != NULL) {
    node *tmp = cursor->next;
    free(cursor);
    cursor = tmp;
  }
  free(l);
}

int list_prepnd(list *l, void *data) {
  node *n = calloc(sizeof(node));
  if(n == NULL) {
    return -1;
  }
  
  if(l->first == NULL) {
    // First element
    l->head = n;
    l->tail = n;
  } else {
    l->head->prev = n;
    l->head = n;
  }
  ++(l->size);
  return 0;
}

void list_append(list *l, void *data) {
  node *n = calloc(sizeof(node));
  if(n == NULL) {
    return -1;
  }
  if(l->last == NULL) {
    // First element
    l->head = n;
    l->tail = n;
  } else {
    l->tail->next = n;
    l->tail = n;
  }
  ++(l->size);
  return 0;
}

void *list_pop(list *l, size_t idx) {
  // Out of bounds
  if(idx > l->size - 1 || idx < -(l->size)) {
    return NULL;
  }

  if(idx < 0) {
    // Reverse if negative
    idx = l->size + idx;
  }

  /* if(idx == 0) { */
  /*   node *n = l->head; */
  /*   --(l->size); */
  /*   l->head = n->next; */
  /*   if(n->next == NULL) */
  /*     l->tail = n->prev; */

  /*   void *data = n->data; */
  /*   free(n); */
  /*   return data; */
  /* } */

  /* if(idx == l->size - 1) { */
  /*   node *n = l->tail; */
  /*   --(l->size); */
  /*   l->tail = n->prev; */
  /*   if(n->prev == NULL) */
  /*     l->head = n->next; */
    
  /*   void *data = n->data; */
  /*   free(n); */
  /*   return data; */
  /* } */

  short search_fwd = idx < l->size / 2;
  void *data = NULL;
  node *cursor = NULL;
  
  // IF idx < l->size/2
  //   search head -> tail
  if(search_fwd) {
    cursor = l->head;
    for(int i = 0; i < idx; ++i) {
      cursor = cursor->next;
    }
  }
  // IF idx > l->size/2
  //   search tail -> head
  else {
    cursor = l->tail;
    for(int i = 0; i > idx; --i) {
      cursor = cursor->prev;
    }
  }

  return data;
}
