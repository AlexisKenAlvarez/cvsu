package countingsort;

/**
 *
 * @author ASUS
 */
import java.util.Arrays;
public class CountingSort {
    public static void main(String[] args) {
        int[] arr = {1,4,1,2,7,5,2};
        
        count(arr);
        
    }
    public static int count(int[] arr) {
        int[] newArr = new int[10];
        int[] finalArr = new int[arr.length];
        int firstNum = 0;
        int len = arr.length;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < len + 1; j++) {
                if (j == arr[firstNum]) {
                newArr[arr[firstNum]] += 1;
                }
            }
        firstNum++;
        }
        
        int index = 0;
        for (int i = 1; i < newArr.length; i++) {
            newArr[i] = newArr[index] + newArr[i];
            index++;
        }
        

        for (int i = arr.length - 1; i != -1; i--) {
            finalArr[newArr[arr[i]] - 1] = arr[i];
            newArr[arr[i]] -= 1;
        }

        
        System.out.println(Arrays.toString(finalArr));
        
        return 0;
    }
    
}
