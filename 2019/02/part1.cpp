#include <iostream>

#include "../../utils/utils.h"


using namespace std;


int main()
{
    auto lines = read_lines("input.txt");
    auto parts = split(lines[0], ',');
    auto ram = to_int(parts);

    size_t ptr = 0;

    ram[1] = 12;
    ram[2] = 2;

    while(true) {
        int opcode = ram[ptr];
        if (opcode == 99) {
            break;
        }

        switch(opcode) {
            case 1:
                ram[ram[ptr + 3]] = ram[ram[ptr + 1]] + ram[ram[ptr + 2]];
                break;
            case 2:
                ram[ram[ptr + 3]] = ram[ram[ptr + 1]] * ram[ram[ptr + 2]];
                break;
        }
        ptr += 4;
    }

    cout << ram[0] << endl;
    return 0;
}