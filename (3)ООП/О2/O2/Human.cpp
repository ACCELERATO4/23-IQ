#include "Human.h"
#include <iostream>
#include <sstream>
#include <ctime>

// Конструктор с параметрами по умолчанию
Human::Human(const std::string& surname,
    const std::string& name,
    const std::string& patronymic,
    const std::string& birthDate,
    const std::string& gender,
    const std::string& address) {
    this->surname = surname;
    this->name = name;
    this->patronymic = patronymic;
    this->gender = gender;

    // Установка даты рождения по умолчанию (текущая дата - 30 лет)
    if (birthDate.empty()) {
        time_t now = time(0);
        tm* ltm = localtime(&now);
        int year = 1900 + ltm->tm_year - 30;
        std::ostringstream oss;
        oss << "01.01." << year;
        this->birthDate = oss.str();
    }
    else {
        this->birthDate = birthDate;
    }

    this->address = address;
}

// Проверка корректности пола
bool Human::isValidGender(const std::string& g) const {
    return (g == "мужской" || g == "женский");
}

// Проверка формата даты (дд.мм.гггг)
bool Human::isValidDate(const std::string& date) const {
    if (date.length() != 10) return false;
    if (date[2] != '.' || date[5] != '.') return false;
    // Упрощенная проверка (можно расширить)
    return true;
}

// Ввод данных с проверкой
void Human::inputData() {
    std::cout << "Введите фамилию: ";
    std::cin >> surname;

    std::cout << "Введите имя: ";
    std::cin >> name;

    std::cout << "Введите отчество: ";
    std::cin >> patronymic;

    // Ввод даты с проверкой
    do {
        std::cout << "Введите дату рождения (дд.мм.гггг): ";
        std::cin >> birthDate;
    } while (!isValidDate(birthDate));

    // Ввод пола с проверкой
    do {
        std::cout << "Введите пол (мужской/женский): ";
        std::cin >> gender;
    } while (!isValidGender(gender));

    std::cout << "Введите адрес: ";
    std::cin.ignore();
    std::getline(std::cin, address);
}

// Вывод данных
void Human::displayData() const {
    std::cout << "\nДанные человека:\n"
        << "Фамилия: " << surname << "\n"
        << "Имя: " << name << "\n"
        << "Отчество: " << patronymic << "\n"
        << "Дата рождения: " << birthDate << "\n"
        << "Пол: " << gender << "\n"
        << "Адрес: " << address << "\n";
}