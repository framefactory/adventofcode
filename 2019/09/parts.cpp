#include <iostream>
#include <vector>

#include "../../utils/utils.h"

using namespace std;

struct instruction_t
{
    int opcode;
    int mode[3];
};

struct state_t
{
    vector<int64_t> ram;
    size_t ptr;

    vector<int64_t> input;
    size_t inPtr;

    vector<int64_t> output;

    int64_t relativeBase;
    bool terminated;

    int64_t read(size_t ptr, size_t mode)
    {
        size_t address = ptr;

        if (mode == 0) {
            address = ram[ptr];
        }
        else if (mode == 2) {
            address = ram[ptr] + relativeBase;
        }
        else if (mode > 2) {
            cout << "invalid mode: " << mode << endl;
            exit(-1);
        }

        if (address >= ram.size()) {
            ram.resize(address + 1, 0);
        }

        return ram[address];
    }

    void write(size_t ptr, size_t mode, int64_t value)
    {
        size_t address = ram[ptr];

        if (mode == 2) {
            address = ram[ptr] + relativeBase;
        }
        else if (mode > 2) {
            cout << "invalid mode: " << mode << endl;
            exit(-1);
        }

        if (address >= ram.size()) {
            ram.resize(address + 1, 0);
        }

        ram[address] = value;
    }
};

instruction_t decode(int64_t code)
{
    string s = to_string(code);
    int l = (int)s.size();

    instruction_t i;
    i.opcode = stoi(s.substr(max(0, l-2), min(l, 2)));
    i.mode[0] = l-3 < 0 ? 0 : s[l-3] - '0';
    i.mode[1] = l-4 < 0 ? 0 : s[l-4] - '0';
    i.mode[2] = l-5 < 0 ? 0 : s[l-5] - '0';

    return i;
}

void compute(state_t& state, bool interrupt = false)
{
    while(true) {
        auto& ptr = state.ptr;
        int64_t code = state.ram[ptr];
        auto i = decode(code);

        if (i.opcode == 99) {
            state.terminated = true;
            return;
        }

        switch(i.opcode) {
        case 1: // add

            state.write(ptr + 3, i.mode[2], state.read(ptr + 1, i.mode[0]) + state.read(ptr + 2, i.mode[1]));
            ptr += 4;
            break;
        case 2: // mul
            state.write(ptr + 3, i.mode[2], state.read(ptr + 1, i.mode[0]) * state.read(ptr + 2, i.mode[1]));
            ptr += 4;
            break;
        case 3: // input
            state.write(ptr + 1, i.mode[0], state.input[state.inPtr++]);
            ptr += 2;
            break; 
        case 4: // output
            state.output.push_back(state.read(ptr + 1, i.mode[0]));
            ptr += 2;
            if (interrupt) {
                state.terminated = false;
                return;
            }
            break;
        case 5: // jump-if-true
            ptr = state.read(ptr + 1, i.mode[0]) != 0 ? state.read(ptr + 2, i.mode[1]) : ptr + 3;
            break;
        case 6: // jump-if-false
            ptr = state.read(ptr + 1, i.mode[0]) == 0 ? state.read(ptr + 2, i.mode[1]) : ptr + 3;
            break;
        case 7: // less-than
            state.write(ptr + 3, i.mode[2], state.read(ptr + 1, i.mode[0]) < state.read(ptr + 2, i.mode[1]) ? 1 : 0);
            ptr += 4;
            break;
        case 8: // equals
            state.write(ptr + 3, i.mode[2], state.read(ptr + 1, i.mode[0]) == state.read(ptr + 2, i.mode[1]) ? 1 : 0);
            ptr += 4;
            break;
        case 9: // relative base
            state.relativeBase += state.read(ptr + 1, i.mode[0]);
            ptr += 2;
            break;
        default:
            cout << "invalid opcode: " << i.opcode << endl;
            exit(-1);
        }
    }
}

int main()
{
    auto lines = read_lines("input.txt");
    auto parts = split(lines[0], ',');
    auto rom = to_bigint(parts);

    // part 1
    state_t state1 {rom, 0, {1}, 0, {}, 0, false};
    compute(state1);

    for (auto output : state1.output) {
        cout << output << endl;
    }

    // part 2
    state_t state2 {rom, 0, {2}, 0, {}, 0, false};
    compute(state2);

    for (auto output : state2.output) {
        cout << output << endl;
    }
}