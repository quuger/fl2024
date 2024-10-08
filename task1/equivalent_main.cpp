#include <iostream>
#include <fstream>
#include <sstream>
#include "machine.hpp"

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Invalid number of arguments\n";
    }
    std::ifstream ifs1(argv[1], std::ios::binary);
    std::ifstream ifs2(argv[2], std::ios::binary);

    machine::solve_equivalent(ifs1, ifs2);
    return 0;
}

//int main(int argc, char* argv[]) {
//    if (argc != 3) {
//        std::cerr << "Invalid number of arguments\n";
//    }
//    machine::solve_equivalent(argv[1], argv[2]);
//    return 0;
//}
//
//void solve_equivalent(char *file1, char *file2) {
//    Machine dfa1, dfa2;
//
//    std::ifstream ifs1(file1, std::ios::binary);
//    dfa1.read(ifs1);
//    ifs1.close();
//
//    std::ifstream ifs2(file2, std::ios::binary);
//    dfa2.read(ifs2);
//    ifs2.close();
//
//    std::cout << std::boolalpha << (dfa1 == dfa2);
//}
