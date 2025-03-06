#include <cmath>
#include "module3.h"

double calculate_y3(double x, double a) {
    double product = 1.0;
    for (int n = 0; n <= 10; ++n) {
        product *= (n * n - a) / x;
    }
    return product;
}