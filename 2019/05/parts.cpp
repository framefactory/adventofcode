#include <iostream>
#include "../../utils/utils.h"

using namespace std;

struct instruction_t
{
    int opcode;
    int mode[3];
};

instruction_t decode(int code)
{
    string s = to_string(code);
    int l = (int)s.size();

    instruction_t i;
    i.opcode = stoi(s.substr(max(0, l-2), min(l, 2)));
    i.mode[0] = l-3 < 0 || s[l-3] == '0' ? 0 : 1;
    i.mode[1] = l-4 < 0 || s[l-4] == '0' ? 0 : 1;
    i.mode[2] = l-5 < 0 || s[l-5] == '0' ? 0 : 1;

    return i;
}

int param(const vector<int>& ram, size_t ptr, size_t mode)
{
    return mode == 0 ? ram[ram[ptr]] : ram[ptr];
}

void compute(vector<int>& ram, const vector<int>& input, size_t ptr = 0)
{
    int inPtr = 0;

    while(true) {
        int code = ram[ptr];
        auto i = decode(code);

        if (i.opcode == 99) {
            return;
        }

        switch(i.opcode) {
        case 1: // add
            ram[ram[ptr + 3]] = param(ram, ptr + 1, i.mode[0]) + param(ram, ptr + 2, i.mode[1]);
            ptr += 4;
            break;
        case 2: // mul
            ram[ram[ptr + 3]] = param(ram, ptr + 1, i.mode[0]) * param(ram, ptr + 2, i.mode[1]);
            ptr += 4;
            break;
        case 3: // input
            ram[ram[ptr + 1]] = input[inPtr++];
            ptr += 2;
            break; 
        case 4: // output
            std::cout << param(ram, ptr + 1, i.mode[0]) << endl;
            ptr += 2;
            break;
        case 5: // jump-if-true
            ptr = param(ram, ptr + 1, i.mode[0]) != 0 ? param(ram, ptr + 2, i.mode[1]) : ptr + 3;
            break;
        case 6: // jump-if-false
            ptr = param(ram, ptr + 1, i.mode[0]) == 0 ? param(ram, ptr + 2, i.mode[1]) : ptr + 3;
            break;
        case 7: // less-than
            ram[ram[ptr + 3]] = param(ram, ptr + 1, i.mode[0]) < param(ram, ptr + 2, i.mode[1]) ? 1 : 0;
            ptr += 4;
            break;
        case 8: // equals
            ram[ram[ptr + 3]] = param(ram, ptr + 1, i.mode[0]) == param(ram, ptr + 2, i.mode[1]) ? 1 : 0;
            ptr += 4;
            break;
        default:
            std::cout << "invalid opcode: " << i.opcode << endl;
            exit(-1);
        }
    }
}

int main()
{
    auto lines = read_lines("input.txt");
    auto parts = split(lines[0], ',');
    auto rom = to_int(parts);

    auto ram1 = rom;
    std::vector<int> input1 = { 1 };
    compute(ram1, input1);

    auto ram2 = rom;
    std::vector<int> input2 = { 5 };
    compute(ram2, input2);
}