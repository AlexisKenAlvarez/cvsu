public class SelectionSort2D {
    public static void sort(int[][] arr){
        Integer[] oneDArray = new Integer[arr.length * arr[0].length];
        int g = 0;
        for(int i = 0; i < arr.length; i ++)
          {
            for(int s = 0; s < arr[0].length; s ++)
            {
              oneDArray[(i * arr[0].length) + s] = arr[i][s];
            }
        }
       
        for (int x = 0; x < oneDArray.length - 1; x++) {
           int lowest = x;
           for (int j = x + 1; j < oneDArray.length; j++) {
               if (oneDArray[j].compareTo(oneDArray[lowest]) < 0) {
                   lowest = j;
                }
           }
           Integer temp = oneDArray[x];
           oneDArray[x] = oneDArray[lowest];
           oneDArray[lowest] = temp;
           
       }

        for(int i = 0; i < arr.length; i ++) 
              for(int j = 0; j < arr[i].length; j ++){                           
                  arr[i][j] = oneDArray[g];
                  g++;
              } 
    }
    
}
