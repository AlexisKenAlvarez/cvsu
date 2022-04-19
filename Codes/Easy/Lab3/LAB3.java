import java.util.Scanner;

public class LAB3 {
    public static void main(String[] args) {
        // SCANNER OBJECT
        Scanner obj = new Scanner(System.in);

        // VARIABLES & INPUT
        System.out.print("Enter first age: ");
        int p1 = obj.nextInt();

        System.out.print("Enter second age: ");
        int p2 = obj.nextInt();

        System.out.print("Enter third age: ");
        int p3 = obj.nextInt();

        // ALGORITHM
        if (p1 > p2) {
            if (p1 > p3) {
                if (p2 > p3) {
                    System.out.println("Oldest is: " + p1);
                    System.out.println("Youngest is: " + p3);
                } else {
                    System.out.println("Oldest is: " + p1);
                    System.out.println("Youngest is: " + p2);
                }
            } else {
                System.out.println("Oldest is: " + p3);
                System.out.println("Youngest is: " + p2);
            }
        }else if (p1 < p2){
            if (p2 > p3){
                if (p1 < p3){
                    System.out.println("Oldest is: " + p2);
                    System.out.println("Youngest is: " + p1);
                }else {
                    System.out.println("Oldest is: " + p2);
                    System.out.println("Youngest is: " + p3);
                }
            }else {
                System.out.println("Oldest is: " + p3);
                System.out.println("Youngest is: " + p1);
            }
        } else if (p1 == p2) {
            if (p1 > p3) {
                System.out.println("Oldest is: " + p1);
                System.out.println("Youngest is: " + p3);
            } else {
                System.out.println("Oldest is: " + p3);
                System.out.println("Oldest is: " + p1);
            }
        }

        obj.close();

    }
    
}
