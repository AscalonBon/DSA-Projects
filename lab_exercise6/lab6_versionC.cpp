#include <iostream>
#include <limits>
using namespace std;

struct CDAccount {
  double balance;
  double interestRate;
  int term;
};

CDAccount doubleInterest(CDAccount oldAccount);
void accountBalance(CDAccount& _account);

void validateInput(double& value, const string& prompt);
void validateInput(int& value, const string& prompt);

int main() {
  CDAccount account;
  validateInput(account.balance, "Enter account balance: Php ");
  validateInput(account.interestRate, "Enter account interest rate: ");
  validateInput(account.term, "Enter the number of months until maturity: ");
  accountBalance(account);
  cout << "\nOld Account\n"
       << "When your CD matures in \n"
       << account.term << " months,\n"
       << "it will have a balance of Php "
       << account.balance << endl;
  CDAccount accountNew;
  accountNew = doubleInterest(account);
  accountBalance(accountNew);
  cout << "\nNew Account\n"
       << "When your CD matures in \n"
       << accountNew.term << " months,\n"
       << "it will have a balance of Php "
       << accountNew.balance << endl;
  system("pause>0");
  return 0;
}

void accountBalance(CDAccount& _account) {
  double rateFraction, interest;
  rateFraction = _account.interestRate / 100.0;
  interest = _account.balance * (rateFraction * (_account.term / 12.0));
  _account.balance = _account.balance + interest;
}

CDAccount doubleInterest(CDAccount oldAccount) {
  CDAccount temp;
  temp = oldAccount;
  temp.interestRate = 2 * oldAccount.interestRate;
  return temp;
}

void validateInput(double& value, const string& prompt) {
  while (true) {
    cout << prompt;
    cin >> value;
    if (cin.fail() || value < 0) {
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
      cout << "Invalid input. Please enter a valid positive number.\n";
    } else {
      break;
    }
  }
}

void validateInput(int& value, const string& prompt) {
  while (true) {
    cout << prompt;
    cin >> value;
    if (cin.fail() || value < 0) {
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
      cout << "Invalid input. Please enter a valid positive integer.\n";
    } else {
      break;
    }
  }
}
