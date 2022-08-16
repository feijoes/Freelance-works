import java.util.Arrays;
public class MyClass {
    public static void main(String args[]) {
      
      int array[] = {2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9};
      
      System.out.println(sumgroups(array));
    
      
    };
    public static int[] removeTheElement(int[] arr, int index)
    {
        if (arr == null || index < 0
            || index >= arr.length) {
 
            return arr;
        }
 
        int[] anotherArray = new int[arr.length - 1];
 
        for (int i = 0, k = 0; i < arr.length; i++) {

            if (i == index) {
                continue;
            }
            anotherArray[k++] = arr[i];
        }
        return anotherArray;
    }
    static int sumgroups(int[] array){
        
        int lenght = array.length;
        int newarray[] =  Arrays.copyOf(array, array.length);
        int a[] = new int[array.length];
        
        System.out.println(Arrays.toString(array));
        
        boolean activate = true;
        
        while (activate){
            
            activate = false;
            
            for (int i=0;i < newarray.length;i++){
                
                int current_sum = newarray[i];
                int start =  newarray[i];
                
                for (int j=i+1;j < newarray.length;j++){
                    
                    if (newarray[i] % 2 != newarray[j] % 2){
                        j=newarray.length +1;
                        continue;
                    }
                    
                    current_sum += array[j];
                   
                    newarray = removeTheElement(newarray,j);
                    activate=true;
                }
            
                a[i] = current_sum;
                
                
            }
            if (activate == false){break;}
        }
        System.out.println(Arrays.toString(a));
        return array.length;
    };
}