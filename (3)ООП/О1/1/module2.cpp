#include <cmath>
#include "module2.h"

double calculate_y2(double x, double a) {
    return log(fabs(x * x - a * a));
}