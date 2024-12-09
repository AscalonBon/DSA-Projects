#include <iostream> 
using namespace std;

//Certificate of Deposit Account Structure
struct CDAccount
{
    double balance;
    double interestRate;
    int term;
};

CDAccount doubleInterest(CDAccount oldAccount);

void accountBalance(CDAccount& _account);

int main()
{
    CDAccount account;
    cout << "Enter account balance: PhP ";
    cin >> account.balance;
    cout << "Enter account interest: ";
    cin >> account.interestRate;
    cout << "Enter number of months until maturity: ";
    cin >> account.term;

    accountBalance(account);

    cout << "\n Old Account \n"
            <<"When your CD matures in \n"
            << account.term << "months,\n"
            <<"it will have a balance of PhP"
            << account.balance << endl;

    CDAccount accountNew;
    accountNew = doubleInterest(account);

    accountBalance(accountNew);

    cout << "\n New Account \n"
            <<"When your CD matures in \n"
            << accountNew.term << "months,\n"
            <<"it will have a balance of PhP"
            << accountNew.balance << endl;

    system("pause>0");
    return 0;

}

CDAccount newAccount (CDAccount newAccount)
{
    double rateFraction, interest;
    rateFraction = newAccount.interestRate/100.0;
    interest = newAccount.balance*(rateFraction*(newAccount.term/12.0));
    newAccount.balance - newAccount.balance + interest;
}

CDAccount oldAccount (CDAccount oldAccount)
{
   CDAccount temp;
   temp = oldAccount;
   temp.interestRate = 2*oldAccount.interestRate;
   return temp;
}


