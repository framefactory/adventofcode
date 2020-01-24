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
    vector<int> ram;
    size_t ptr;

    vector<int> input;
    size_t inPtr;

    vector<int> output;
    bool terminated;
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

void compute(state_t& state, bool interrupt = false)
{
    auto& ram = state.ram;
    auto& ptr = state.ptr;

    while(true) {
        int code = ram[state.ptr];
        auto i = decode(code);

        if (i.opcode == 99) {
            state.terminated = true;
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
            ram[ram[ptr + 1]] = state.input[state.inPtr++];
            ptr += 2;
            break; 
        case 4: // output
            state.output.push_back(param(ram, ptr + 1, i.mode[0]));
            ptr += 2;
            if (interrupt) {
                state.terminated = false;
                return;
            }
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

void permute(vector<vector<int>>& permutations, vector<int>& elements, int k)
{
    if (k == 0) {
        permutations.push_back(elements);
        return;
    }

    permute(permutations, elements, k - 1);

    for (int i = 0; i < k; ++i) {
        if (k % 2 == 0) {
            swap(elements[0], elements[k]);
        }
        else {
            swap(elements[i], elements[k]);
        }
        permute(permutations, elements, k - 1);
    }
}

int part1(const vector<int>& rom)
{
    vector<int> sequence = {0, 1, 2, 3, 4};
    vector<vector<int>> permutations;
    permute(permutations, sequence, sequence.size() - 1);

    int max_signal = 0;

    for (auto sequence : permutations) {
        int signal = 0;

        for (auto phase : sequence) {
            vector<int> input {phase, signal};
            state_t state {rom, 0, input, 0, vector<int>{}};
            compute(state);
            signal = state.output[0];
        }

        if (signal > max_signal) {
            max_signal = signal;
        }
    }

    return max_signal;
}

int part2(const vector<int>& rom)
{
    vector<int> sequence {5, 6, 7, 8, 9};
    vector<vector<int>> permutations;
    permute(permutations, sequence, sequence.size() - 1);

    int max_signal = 0;

    for (auto sequence : permutations) {
        int signal = 0;
        vector<state_t> states;
        for (int amp = 0; amp < 5; ++amp) {
            states.push_back(state_t{ rom, 0, {sequence[amp]}, 0, {}, false });
        }

        bool terminated = false;

        while(!terminated) {
            for (int amp = 0; amp < 5; ++amp) {
                if (states[amp].terminated) {
                    terminated = true;
                }

                states[amp].input.push_back(signal);
                compute(states[amp], true);
                signal = states[amp].output[0];
                states[amp].output.clear();
            }

            if (signal > max_signal) {
                max_signal = signal;
            }
        }
    }

    return max_signal;
}

int main()
{
    auto lines = read_lines("input.txt");
    auto parts = split(lines[0], ',');
    auto rom = to_int(parts);

    cout << "Part 1: " << part1(rom) << endl;
    cout << "Part 2: " << part2(rom) << endl;
}