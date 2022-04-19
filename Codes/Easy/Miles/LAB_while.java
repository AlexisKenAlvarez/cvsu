import java.util.Scanner;

public class LAB_while {
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
        
        // INPUT
        System.out.print("Enter distance in miles: ");
        int miles = obj.nextInt();

        int one = 1;
        
        // CONDITION AND WHILE LOOP
        if (miles > 0) {
            System.out.println("\nmiles(mi)\tyards(yd)\tkilometers(km)\n");
            while (one < 11) {
                System.out.println(miles + "\t\t" + (miles * 1760) + "\t\t" + (miles * 1.60934));
                miles++;
                one++;
            }
        } else if (miles <= 0) {
            System.out.println("Invalid input!");
        }
        
        // OBJ CLOSED
        obj.close();
    }
}


