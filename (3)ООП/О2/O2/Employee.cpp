#include "Employee.h"
#include <iostream>

Employee::Employee(const std::string& position) : Human() {
    this->position = position;
}

void Employee::inputPosition() {
    std::cout << "Введите должность: ";
    std::cin.ignore();
    std::getline(std::cin, position);
}

void Employee::displayPosition() const {
    std::cout << "Должность: " << position << "\n";
}