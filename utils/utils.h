#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const vector<string> read_lines(const string& filename)
{
    ifstream file;
    file.open(filename, ios::in);

    if (!file.is_open()) {
        cerr << "error opening input file." << endl;
        exit(-1);
    }

    string line;
    std::vector<string> input;

    while(getline(file, line)) {
        input.push_back(line);
    }

    file.close();
    return input;
}

const string read_all(const string& filename)
{
    ifstream file;
    file.open(filename, ios::in);

    if (!file.is_open()) {
        cerr << "error opening input file." << endl;
        exit(-1);
    }

    stringstream buffer;
    buffer << file.rdbuf();

    file.close();
    return buffer.str();
}

const vector<int> to_int(const vector<string>& strings)
{
    vector<int> numbers;
    numbers.reserve(strings.size());

    for (auto s : strings) {
        numbers.push_back(stoi(s));
    }

    return numbers;
}

const vector<double> to_float(const vector<string>& strings)
{
    vector<double> numbers;
    numbers.reserve(strings.size());

    for (auto s: strings) {
        numbers.push_back(stod(s));
    }

    return numbers;
}

const vector<string> split(const string& text, const char& separator = ' ')
{
    size_t length = text.size();
    size_t pos = 0;
    vector<string> result;

    for (size_t i = 0; i < length; ++i) {
        if (text[i] == separator) {
            result.push_back(text.substr(pos, i - pos));
            pos = i + 1;
        }
    }

    result.push_back(text.substr(pos, length - pos));
    return result;
}
