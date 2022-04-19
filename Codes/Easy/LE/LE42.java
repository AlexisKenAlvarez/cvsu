import java.util.Scanner;

public class LE42 {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        // VARIABLES
        System.out.print("Enter num1: ");
        int A = obj.nextInt();

        System.out.print("Enter num2: ");
        int B = obj.nextInt();

        System.out.print("Enter num3: ");
        int C = obj.nextInt();


        // OPERATION
        if (A == B) {
            System.out.println("!-ERROR-! A number is repeated! !-ERROR-!");
        }
        else if (A == C) {
            System.out.println("!-ERROR-! A number is repeated! !-ERROR-!");
        }
        else if (B == C) {
            System.out.println("!-ERROR-! A number is repeated! !-ERROR-!");
        }
        else if (A == B && A == C && B == C) {
            System.out.println("!-ERROR-! A number is repeated! !-ERROR-!");
        }
        else {
            if (A > B) {
                if (A > C) {
                    System.out.println(A + " is the highest number!");
                } else {
                    System.out.println(C + " is the highest number!");
                }
            } else if (A < B) {
                if (B > C) {
                    System.out.println(B + " is the highest number!");
                } else {
                    System.out.println(C + " is the highest number!");
                }
            }
        }

        // SCANNER OBJECT CLOSED
        obj.close();
    }
}