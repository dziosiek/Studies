public class MaxSum {
    public static void main(String[] args) {
        int mainMax = 0, localMax = 0;
        int[] array = {1, 4, 5, -4, 1};
        for (int i = 0; i < array.length; i++) {
            localMax += array[i];
            if(localMax > mainMax) mainMax = localMax;
            else if(localMax<0) localMax = 0;
        }
        System.out.println(mainMax);
    }
}
