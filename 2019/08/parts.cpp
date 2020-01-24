#include <iostream>
#include <limits>

#include "../../utils/utils.h"

int main()
{
    auto lines = read_lines("input.txt");
    vector<char> digits;

    for (auto c : lines[0]) {
        if (c >= '0' && c <= '9') {
            digits.push_back(c - '0');
        }
    }

    size_t digits_count = digits.size();
    size_t width = 25;
    size_t height = 6;
    size_t layer_size = width * height;
    size_t layer_count = digits.size() / layer_size;

    // part 1
    vector<int[10]> layers(layer_count);

    for (size_t i = 0; i < digits_count; ++i) {
        layers[i / layer_size][digits[i]]++;
    }

    size_t id = 0;
    int zeroes = numeric_limits<int>::max();

    for (size_t i = 0; i < layer_count; ++i) {
        if (layers[i][0] < zeroes) {
            zeroes = layers[i][0];
            id = i;
        }
    }

    cout << layers[id][1] * layers[id][2] << endl;

    // part 2
    vector<int> image(layer_size);

    for (size_t c = 0; c < height; ++c) {
        for (size_t r = 0; r < width; ++r) {
            int i = c * width + r;

            int color = 2;
            for (size_t l = 0; l < layer_count; ++l) {
                color = digits[l * layer_size + i];
                if (color < 2) {
                    break;
                }
            }
            image.push_back(color);
            cout << (color == 1 ? "X" : " ");
        }
        cout << endl;
    }
}