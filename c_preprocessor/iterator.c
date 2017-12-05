
#define SUB2(x,y) SUB(x) ## - ## SUB(y)
#define SUB(x) x ## -1


SUB2(3, 4)
