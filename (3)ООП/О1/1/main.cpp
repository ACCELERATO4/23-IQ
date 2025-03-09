#include <iostream>
#include <cmath>
#include "module1.h"
#include "module2.h"
#include "module3.h"

using namespace std;

int main() {
    const double a = 1.25;
    const double b = 6.3;
    const double x_H = 0.4;
    const double x_K = 10.3;
    const double delta_x = 0.8;

    for (double x = x_H; x <= x_K; x += delta_x) {
        if (x < a) {
            cout << "x = " << x << ", y = " << calculate_y1(x, a, b) << endl;
        }
        else if (x >= a && x < b) {
            cout << "x = " << x << ", y = " << calculate_y2(x, a) << endl;
        }
        else if (x > 9.1) { // Условие по заданию
            cout << "x = " << x << ", y = " << calculate_y3(x, a) << endl;
        }
        else {
            cout << "x = " << x << ", y = undefined" << endl;
        }
    }

    return 0;
}