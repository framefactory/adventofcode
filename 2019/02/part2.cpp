#include <iostream>

#include "../../utils/utils.h"

using namespace std;

int main()
{
    auto lines = read_lines("input.txt");
    auto parts = split(lines[0], ',');
    auto rom = to_int(parts);

    for (int noun = 0; noun < 100; ++noun) {
        for (int verb = 0; verb < 100; ++verb) {
            auto ram = rom;
            ram[1] = noun;
            ram[2] = verb;

            size_t ptr = 0;
            while (true) {
                int opcode = ram[ptr];
                if (opcode == 99) {
                    break;
                }

                switch (opcode) {
                case 1:
                    ram[ram[ptr + 3]] = ram[ram[ptr + 1]] + ram[ram[ptr + 2]];
                    break;
                case 2:
                    ram[ram[ptr + 3]] = ram[ram[ptr + 1]] * ram[ram[ptr + 2]];
                    break;
                }
                ptr += 4;
            }

            if (ram[0] == 19690720) {
                cout << 100 * noun + verb << endl;
                return 0;
            }
        }
    }

    return 0;
}