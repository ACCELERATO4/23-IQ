#include <cmath>
#include "module1.h"

double calculate_y1(double x, double a, double b) {
    double numerator = 3 * (exp(a * x) - b);
    double denominator = pow(cos(a + b * x), 2);
    return numerator / denominator;
}