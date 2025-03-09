#include "Human.h"
#include "Employee.h"
#include <iostream>

int main() {
    // Тест базового класса
    Human human;
    std::cout << "Ввод данных для человека:\n";
    human.inputData();
    human.displayData();

    // Тест производного класса
    Employee employee;
    std::cout << "\nВвод данных для сотрудника:\n";
    employee.inputData(); // Метод из базового класса
    employee.inputPosition();
    employee.displayData(); // Метод из базового класса
    employee.displayPosition();

    return 0;
}