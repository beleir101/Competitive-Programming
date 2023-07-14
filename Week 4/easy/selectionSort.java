package easy;

public class selectionSort {
    void selectionSort(int arr[], int n)
    {
        //code here
        for (int i = 0; i < n; i++) {
            int[] min = new int[2];
            min[0] = Integer.MAX_VALUE;
            for (int j = i; j < n; j++) {
                if (arr[j] < min[0]){
                    min[0] = arr[j];
                    min[1] = j;
                }
            }
            int temp = arr[min[1]];
            arr[min[1]] = arr[i];
            arr[i] = temp;
        }
    }
}
