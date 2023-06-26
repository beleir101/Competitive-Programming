package Week1;
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class HR_Counting_Sort1 {


        /*
         * Complete the 'countingSort' function below.
         *
         * The function is expected to return an INTEGER_ARRAY.
         * The function accepts INTEGER_ARRAY arr as parameter.
         */

        public static List<Integer> countingSort(List<Integer> arr) {
            //write your code here
            List<Integer> sorted = new ArrayList<Integer>();
            for (int i = 0; i < 100; i++){
                sorted.add(0);
            }
            for (int k : arr){
                sorted.set(k, sorted.get(k) + 1);
            }
            System.out.println(sorted);
            return sorted;
        }

    }

