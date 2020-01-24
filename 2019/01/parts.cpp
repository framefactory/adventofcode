#include <iostream>

#include "../../utils/utils.h"


using namespace std;

int get_fuel(int mass, bool recursive = false)
{
    int fuel = max(0, mass / 3 - 2);

    if (recursive && fuel > 0) {
        fuel += get_fuel(fuel);
    }

    return fuel;
}

int main(int argc, char** ppArgv)
{
    auto lines = read_lines("input.txt");
    auto masses = to_int(lines);

    int total_fuel = 0;
    int total_fuel_recursive = 0;

    for (auto m : masses) {
        total_fuel += get_fuel(m, false);
        total_fuel_recursive += get_fuel(m, true);
    }

    cout << "Part 1: " << total_fuel << endl;
    cout << "Part 2: " << total_fuel_recursive << endl;

    return 0;
}