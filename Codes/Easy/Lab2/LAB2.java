import java.util.Scanner;

public class LAB2{
    public static void main(String[] args) {
        // SCANNER OBJECT
        Scanner obj = new Scanner(System.in);


        // VARIABLES FOR P1 AND P2
        System.out.print("Enter player 1 score: ");
        int p1 = obj.nextInt();

        obj.nextLine();

        System.out.print("Enter player 2 score: ");
        int p2 = obj.nextInt();


        // ALGORITHM 
        if (p1 > p2) {
            System.out.println("Player 1 won!");
        } else if (p1 < p2){
            System.out.println("Player 2 won!");
        } else {
            System.out.println("It's a tie!");
        }

        obj.close();

    }
}