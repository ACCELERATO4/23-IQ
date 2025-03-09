#ifndef EMPLOYEE_H
#define EMPLOYEE_H
#include "Human.h"

class Employee : public Human {
private:
    std::string position;

public:
    Employee(const std::string& position = "");
    void inputPosition();
    void displayPosition() const;
};

#endif