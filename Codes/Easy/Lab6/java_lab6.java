import java.util.Scanner;

public class java_lab6 {
    public static void main(String[] args) {

        Scanner obj = new Scanner(System.in);

        System.out.println("---EXPONENT CALCULATOR---");

        System.out.print("Enter a number: ");
        int num = obj.nextInt();

        System.out.print("Enter exponent: ");
        int exp = obj.nextInt();

        int value = num;

        if (exp > 0) {          // Checks if exponent is greater than zero
            for (int i = 1; i < 2; i++) {           
                for (int x = 1; x < exp; x++) {         // Multiplies to itself based on the number of exponent
                    num = num * value;

                }
            }

            System.out.println("\nThe answer is " + num);   
        } else if (exp == 0) {          // Checks if exponent is equal to zero because the answer will be always 1 if true
            System.out.println("\nThe answer is 1");        
        }
        else {
            System.out.println("\nInvalid input. This program does not support that input yet.");
        }

        obj.close();            // Closes the obj

    }
}
