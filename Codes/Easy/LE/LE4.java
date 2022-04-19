import java.util.Scanner;

public class LE4 {

    static int add(int a, int b) {
        return a + b;
    }

    static int minus(int a, int b) {
        return a - b;
    }

    static int multi(int a, int b) {
        return a * b;
    }

    static int div(int a, int b) {
        return a / b;
    }

    static int mod(int a, int b) {
        return a % b;
    }
        
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        // Variables
        System.out.print("Enter num1: ");
        int num1 = obj.nextInt();

        System.out.print("Enter num2: ");
        int num2 = obj.nextInt();

        System.out.print("Choose operator \n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Modulo\n:");
        int opr = obj.nextInt();

        // Operation
        if (opr == 1) {
            System.out.println(num1 + " + " + num2 + " = " + add(num1, num2));
        }
        else if (opr == 2) {
            System.out.println(num1 + " - " + num2 + " = " + minus(num1, num2));
        }
        else if (opr == 3) {
            System.out.println(num1 + " * " + num2 + " = " + multi(num1, num2));
        }
        else if (opr == 4) {
            if (num2 == 0) {
                System.out.println("Cannot divide by zero.");
            }
            else {
                System.out.println(num1 + " ÷ " + num2 + " = " + div(num1, num2));
            }
        }
        else if (opr == 5) {
            if (num2 == 0) {
                System.out.println("Result is undefined.");
            } else {
                System.out.println(num1 + " % " + num2 + " = " + mod(num1, num2));
            }
        }
        else {
            System.out.println("Invalid Operator.");
        }
        
        obj.close();
    }
}
