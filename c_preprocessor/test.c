



#define VALUE first

#define PASTER(A,B) A ## _ ## B
#define PASTER__(A,B) A ## _ ## B

#define EXPANDER(A,B) PASTER(A,B)
#define EXPANDER_(A,B) A ## B


=====================================================
 

Value: VALUE
  
EXPANDER_(VALUE, second)
  


EXPANDER(VALUE,second)
