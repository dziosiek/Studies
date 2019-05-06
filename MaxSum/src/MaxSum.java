public class MaxSum {
    public static void main(String[] args) {
        int[] array = {1, 20, -20,22,-23,1,25, -4, 1};
        System.out.println(maxSum(array));
    }
    public static int maxSum(int[] array){
        int mainMax = 0, localMax = 0;

        for (int i = 0; i < array.length; i++) {
            localMax += array[i];
            if(localMax > mainMax) mainMax = localMax;
            else if(localMax<0) localMax = 0;
        }
        return mainMax;
    }
}
