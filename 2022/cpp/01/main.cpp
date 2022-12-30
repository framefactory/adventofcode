#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main(int argc, char** ppArgv)
{
    ifstream file;
    file.open("input.txt", ios::in);
    if (!file) {
        cerr << "failed to open input file" << endl;
        return 1;
    }

    while(file) {
        string line;
        getline(file, line);
    }

    file.read()

    cout << "Hello, world!" << endl;
    return 0;
}