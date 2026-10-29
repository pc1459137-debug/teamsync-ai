#include <iostream>
using namespace std;

int main() {
    int choice;

    cout << "Exception Handling Demo\n";
    cout << "1. Age validation\n";
    cout << "2. Division\n";
    cout << "Enter your choice: ";
    cin >> choice;

    try {
        if (choice == 1) {
            int age;
            cout << "Enter age: ";
            cin >> age;

            if (age < 18) {
                throw age;
            }

            cout << "Age is valid. You are eligible.\n";
        }
        else if (choice == 2) {
            double a, b;
            cout << "Enter two numbers: ";
            cin >> a >> b;

            if (b == 0) {
                throw "Division by zero is not allowed.";
            }

            cout << "Result = " << a / b << '\n';
        }
        else {
            cout << "Invalid choice.\n";
        }
    }
    catch (int age) {
        cout << "Exception caught: Age " << age
             << " is below 18.\n";
    }
    catch (const char* message) {
        cout << "Exception caught: " << message << '\n';
    }

    return 0;
}
