typedef int (*MathFunction)(int, int);

typedef int (*read_callback_t)(uint32_t address, size_t size, uint8_t* dst);
typedef int (*write_callback_t)(uint32_t address, size_t size, uint8_t* src);
typedef struct {
    read_callback_t rcb;
    read_callback_t wcb;
} my_struct_t;

int do_math(MathFunction pMf, int a, int b);

int setup_callbacks(my_struct_t* pMyStruct, read_callback_t rcb, write_callback_t wcb);
int read_from_buffer(my_struct_t* pMyStruct, uint32_t address, size_t size, uint8_t* dst);
int write_to_buffer(my_struct_t* pMyStruct, uint32_t address, size_t size, uint8_t* src);