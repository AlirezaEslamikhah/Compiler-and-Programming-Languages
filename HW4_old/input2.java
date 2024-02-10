// Class representing a BankAccount
class BankAccount {
    private String accountNumber;
    private double balance;

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited $" + amount + " into account " + accountNumber);
    }

    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("Withdrawn $" + amount + " from account " + accountNumber);
        } else {
            System.out.println("Insufficient funds in account " + accountNumber);
        }
    }

    public void displayBalance() {
        System.out.println("Account " + accountNumber + " Balance: $" + balance);
    }
}

// Class representing a Customer that is coupled with the BankAccount class
class Customer {
    private String name;
    private BankAccount account;

    public Customer(String name, BankAccount account) {
        this.name = name;
        this.account = account;
    }

    public void performTransaction(double amount) {
        account.deposit(amount);
        account.withdraw(amount / 2);
        account.displayBalance();
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating an instance of the BankAccount class
        BankAccount account = new BankAccount("123456", 1000.0);

        // Creating an instance of the Customer class and associating it with the BankAccount
        Customer customer = new Customer("John Doe", account);

        // Performing a transaction for the customer
        customer.performTransaction(500.0);
    }
}
