import java.util.Scanner;

public class lab1 {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = obj.nextLine();

        System.out.print("Enter your Student Number: ");
        int SN = obj.nextInt();

        obj.nextLine();

        System.out.print("Enter your course: ");
        String crs = obj.nextLine();

        System.out.print("Enter your E-mail address: ");
        String email = obj.nextLine();

        System.out.println("\n");
        System.out.println("Name: " + name);
        System.out.println("Student Number: " + SN);
        System.out.println("Course: " + crs);
        System.out.println("E-mail address: " + email);
        
        obj.close();
    }
}