public class BinarySearch2D {
    public static int search(int[][] arr, int x){
        int row = arr.length;
        int column = arr[0].length;
        
        int lo = 0;
        int hi = row * column  - 1;
        
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int y = mid / column ;
            int z = mid % column ;
            int midVal = arr[y][z];
            
            if (midVal == x) {
                return mid;
                
            }else if (midVal > x){
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
               
        }
        return -1;
    }
}

    

