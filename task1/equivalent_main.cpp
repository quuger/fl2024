#include <iostream>
#include <fstream>
#include "machine.hpp"

//int main(int argc, char* argv[]) {
//    if (argc != 3) {
//        std::cerr << "Invalid number of arguments\n";
//    }
//    std::ifstream ifs1(argv[1], std::ios::binary);
//    std::ifstream ifs2(argv[2], std::ios::binary);
//
//    machine::solve_equivalent(ifs1, ifs2);
//    return 0;
//}

int main() {
    machine::solve_equivalent();
    return 0;
}