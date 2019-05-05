import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Sum2num {

    private static int[] randomArray(int size){
        /** Method generates random int array with defined size
         */
        Random random = new Random();
        int[] array = new int[size];
        for (int i = 0; i < array.length; i++) {
            array[i] = random.nextInt(30);
        }
        return array;

    }

    private static void quickSort(int arr[], int begin, int end) {
        if (begin < end) {
            int partitionIndex = partition(arr, begin, end);

            quickSort(arr, begin, partitionIndex - 1);
            quickSort(arr, partitionIndex + 1, end);
        }
    }

    private static int partition(int arr[], int begin, int end) {
        int pivot = arr[end];
        int i = (begin - 1);

        for (int j = begin; j < end; j++) {
            if (arr[j] <= pivot) {
                i++;

                int swapTemp = arr[i];
                arr[i] = arr[j];
                arr[j] = swapTemp;
            }
        }

        int swapTemp = arr[i + 1];
        arr[i + 1] = arr[end];
        arr[end] = swapTemp;

        return i + 1;
    }

    private static boolean findSum(int[] s1, int[] s2, int x){
        int left = 0, right = s2.length-1;
        while(left<s1.length && right>=0){
            int result = s1[left] + s2[right];
            if(result==x) {
                System.out.println("s1["+left+"] = " + s1[left]);
                System.out.println("s2["+right+"] = " + s2[right]);
                return true;
//                return true;
            }
            else if(result>x) right--;
            else left++;
        }
        return false;

    }

    public static void main(String[] args) {
        int[] s1 = randomArray(10);
        int[] s2 = randomArray(20);
        int x = 10;
        quickSort(s1,0,s1.length-1);
        quickSort(s2,0,s2.length-1);
        System.out.println(Arrays.toString(s1)+" / " + Arrays.toString(s2));
        System.out.println(findSum(s1, s2, x));









    }
}
