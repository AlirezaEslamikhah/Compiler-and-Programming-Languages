interface Greeting {
    void sayHello();
}

public class HelloWorld implements Greeting {
    private String message;

    public HelloWorld(String message) {
        this.message = message;
    }

    public String getMessage() {
        return this.message;
    }

    public String temp(String x) {
        return this.x;
    }

    @Override
    public void sayHello() {
        System.out.println(this.message);
    }

    public static void main(String[] args,int a) {
        HelloWorld helloWorld = new HelloWorld("Hello, World!");
        helloWorld.sayHello();
        System.out.println(helloWorld.getMessage());
    }
}
