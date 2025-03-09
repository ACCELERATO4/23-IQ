#include "Human.h"
#include <iostream>
#include <sstream>
#include <ctime>

// ����������� � ����������� �� ���������
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

    // ��������� ���� �������� �� ��������� (������� ���� - 30 ���)
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

// �������� ������������ ����
bool Human::isValidGender(const std::string& g) const {
    return (g == "�������" || g == "�������");
}

// �������� ������� ���� (��.��.����)
bool Human::isValidDate(const std::string& date) const {
    if (date.length() != 10) return false;
    if (date[2] != '.' || date[5] != '.') return false;
    // ���������� �������� (����� ���������)
    return true;
}

// ���� ������ � ���������
void Human::inputData() {
    std::cout << "������� �������: ";
    std::cin >> surname;

    std::cout << "������� ���: ";
    std::cin >> name;

    std::cout << "������� ��������: ";
    std::cin >> patronymic;

    // ���� ���� � ���������
    do {
        std::cout << "������� ���� �������� (��.��.����): ";
        std::cin >> birthDate;
    } while (!isValidDate(birthDate));

    // ���� ���� � ���������
    do {
        std::cout << "������� ��� (�������/�������): ";
        std::cin >> gender;
    } while (!isValidGender(gender));

    std::cout << "������� �����: ";
    std::cin.ignore();
    std::getline(std::cin, address);
}

// ����� ������
void Human::displayData() const {
    std::cout << "\n������ ��������:\n"
        << "�������: " << surname << "\n"
        << "���: " << name << "\n"
        << "��������: " << patronymic << "\n"
        << "���� ��������: " << birthDate << "\n"
        << "���: " << gender << "\n"
        << "�����: " << address << "\n";
}