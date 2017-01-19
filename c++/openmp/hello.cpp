#include <iostream>
#include <omp.h>

int main(int argc, char *argv[])
{
    omp_set_num_threads(4);
    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        std::cout << "Hello World " << id << "!\n";
    }
    return 0;
}
