package Week1;
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
public class HR_Bubble_Sort {
    private static int noSwaps = 0;
    public static void countSwaps(List<Integer> a){
        int size = a.size();
        for(int i = 0; i < size; i++){
            for(int k = 0; k < (size - i - 1); k ++) {
                if (a.get(k) > a.get(k + 1)) {
                    int temp = a.get(k);
                    a.set(k, a.get(k + 1));
                    a.set(k + 1, temp);
                    noSwaps++;
                }
            }
        }
        System.out.println("Array is sorted in " + noSwaps +  " swaps.");
        System.out.println("First Element: " + a.get(0));
        System.out.println("Last Element: " + a.get(size - 1));

    }
}
