// Class representing a ShoppingCart
class ShoppingCart {
    private int itemCount;

    public void addItem() {
        itemCount++;
        System.out.println("Item added to the shopping cart. Total items: " + itemCount);
    }

    public void removeItem() {
        if (itemCount > 0) {
            itemCount--;
            System.out.println("Item removed from the shopping cart. Total items: " + itemCount);
        } else {
            System.out.println("Shopping cart is already empty.");
        }
    }
}

// Class representing a Customer that is more tightly coupled with the ShoppingCart class
class Customer {
    private String name;
    private ShoppingCart shoppingCart;

    public Customer(String name) {
        this.name = name;
        this.shoppingCart = new ShoppingCart(); // Tightly coupled instantiation
    }

    public void addItemToCart() {
        shoppingCart.addItem();
    }

    public void removeItemFromCart() {
        shoppingCart.removeItem();
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating an instance of the Customer class
        Customer customer = new Customer("Alice");

        // Performing actions with the customer and shopping cart
        customer.addItemToCart();
        customer.addItemToCart();
        customer.removeItemFromCart();
    }
}
