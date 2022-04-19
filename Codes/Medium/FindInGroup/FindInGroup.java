import java.util.*;

public class FindInGroup{
    public static void main(String[] args){
        Scanner obj = new Scanner(System.in);
        
        // INPUT FOR FIRST LINE
        System.out.print("");
        int group = obj.nextInt();
        int ntoFind = obj.nextInt();

        
        // 2d ARRAY FOR GROUP
        int[][] myArr = new int[group][];
        
        int[] toBeSearched = new int[ntoFind];
        int[] outputArr = new int[ntoFind];
        
        
        // COUNT OF NUMBER OF ELEMENTS TO BE GIVEN TO EACH GROUP
        int count = 0;
        // INPUT FOR 2ND LINE
        System.out.println(" ");
        for (int i = 0; i < group; i++) {
            myArr[i] = new int[obj.nextInt()];
        }
        
        // INCREMENTS TO COUNT 
        for (int i = 0; i < group; i++) {
            count++;
        }

        if (count != group) {
            System.out.println("BAD INPUT");
            System.exit(0);
        }

        // THIRD LINE
        for (int i = 0; i < myArr.length; i++) {
        System.out.println(" ");
            for (int j = 0; j < myArr[i].length; j++) {
                int val = obj.nextInt();
                myArr[i][j] = val;
                
                // CHECKER TO SEE IF AN ELEMENT ALREADY EXIST FROM THE PREVIOUS GROUP
                if (i > 0) {
                    if (output(myArr, val) == -1) {
                    } else if (output(myArr, val) <= i) {
                        System.out.println("An element you entered already exists on the other group.");
                        System.exit(0);
                    }
                } 
            }
        }
        
        // ELEMENTS TO BE SEARCHED
        for (int i = 0; i < ntoFind; i++) {
            System.out.println(" ");
            int intVal = obj.nextInt();
            toBeSearched[i] = intVal;
        }

        // PRINTING OUTPUT
        for (int i = 0; i < ntoFind; i++) {
            outputArr[i] = output(myArr, toBeSearched[i]);
            System.out.println(outputArr[i]);
        }

}
    public static int output(int[][] arr, int num) {
        
                // loop for rows of matrix
        for (int i = 0; i < arr.length; i++) {
 
            // loop for column of matrix
            for (int j = 0; j < arr[i].length; j++) {
 
                // loop for comparison and swapping
                for (int k = 0; k < arr[i].length - j - 1; k++) {
                    if (arr[i][k] > arr[i][k + 1]) {
 
                        // swapping of elements
                        int t = arr[i][k];
                        arr[i][k] = arr[i][k + 1];
                        arr[i][k + 1] = t;
                    }
                }
            }
        }
        
        for (int i = 0; i < arr.length; i++) {
            int left = 0;
            int right = arr[i].length - 1; // 4
            while (left <= right) { // 0 < 4
                int middle = (left + right)/2; // 2

                if (num == arr[i][middle]) { // 1 == ar[0][0] 5 
                    return i + 1;
                } else if (num < arr[i][middle]) {
                    right = middle - 1;
                } else if (num > arr[i][middle]) {
                    left = middle + 1;
                }
            }

        }
        return -1;

    }
}