// Class representing a BankAccount
class BankAccount {
    private String accountNumber;
    private double balance;
    private City city; 
    public BankAccount(String accountNumber, double balance , City city) {
        this.accountNumber = accountNumber;
        this.balance = balance;
        this.customer = customer; 
        this.city = city;
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
}

class City {
    private string name;
    private Customer customer;
    public City(String name , Cutomer customer )
    {
        this.name = name;
        this.customer = customer;
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating an instance of the Customer class and associating it with the BankAccount
        Customer customer = new Customer("John Doe", account);
        City city = new City("tehran" , customer);
        
        
        // Creating an instance of the BankAccount class
        BankAccount account = new BankAccount("123456", 1000.0 , city);
        
        // Performing a transaction for the customer
        customer.performTransaction(500.0);
        
        
    }
}
