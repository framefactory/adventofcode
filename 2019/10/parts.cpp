#include <iostream>
#include <vector>
#include <cmath>

#include "../../utils/utils.h"


int main()
{
    auto belt = read_lines("input.txt");

    int width = belt[0].size();
    int height = belt.size();
    cout << width << " x " << height << endl;

    size_t max_visible = 0;
    int best_x = 0;
    int best_y = 0;

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            if (belt[y][x] != '#') {
                continue;
            }

            size_t visible_count = 0;

            for (int yy = 0; yy < height; ++yy) {
                for (int xx = 0; xx < width; ++xx) {
                    if (belt[yy][xx] != '#' || (yy == y && xx == x)) {
                        continue;
                    }

                    bool blocked = false;
                    int dx = xx - x;
                    int dy = yy - y;

                    if (abs(dx) > abs(dy)) {
                        int step = dx > 0 ? 1 : -1;
                        for (int i = step; i != dx; i += step) {
                            int ix = x + i;
                            double iy = y + dy / double(dx) * i;
                            if (iy == trunc(iy) && belt[int(iy)][ix] == '#') {
                                blocked = true;
                                break;
                            }
                        }
                    }
                    else {
                        int step = dy > 0 ? 1 : -1;
                        for (int i = step; i != dy; i += step) {
                            int iy = y + i;
                            double ix = x + dx / double(dy) * i;
                            if (ix == trunc(ix) && belt[iy][int(ix)] == '#') {
                                blocked = true;
                                break;
                            }
                        }
                    }

                    if (!blocked) {
                        visible_count++;
                    }
                }
            }

            if (visible_count > max_visible) {
                max_visible = visible_count;
                best_x = x;
                best_y = y;
            }
        }
    }

    cout << max_visible << ", (" << best_x << ", " << best_y << ")" << endl;
}