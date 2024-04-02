#include <stdlib.h>
#include <stdint.h>

#include "cfunctions.h"

int do_math(MathFunction pMf, int a, int b)
{
    return pMf(a, b);
}

int setup_callbacks(my_struct_t* pMyStruct, read_callback_t rcb, write_callback_t wcb) {
    pMyStruct->rcb = rcb;
    pMyStruct->wcb = wcb;
    return 1;
}

int read_from_buffer(my_struct_t* pMyStruct, uint32_t address, size_t size, uint8_t* dst) {
    return pMyStruct->rcb(address, size, dst);
}

int write_to_buffer(my_struct_t* pMyStruct, uint32_t address, size_t size, uint8_t* src) {
    return pMyStruct->wcb(address, size, src);
}
