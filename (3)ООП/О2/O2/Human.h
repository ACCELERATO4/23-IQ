#ifndef HUMAN_H
#define HUMAN_H
#include <string>
#include <ctime>

class Human {
protected:
    std::string surname;
    std::string name;
    std::string patronymic;
    std::string birthDate;
    std::string gender;
    std::string address;

    bool isValidGender(const std::string& g) const;
    bool isValidDate(const std::string& date) const;

public:
    Human(const std::string& surname = "",
        const std::string& name = "",
        const std::string& patronymic = "",
        const std::string& birthDate = "",
        const std::string& gender = "мужской",
        const std::string& address = "");

    void inputData();
    void displayData() const;
};

#endif