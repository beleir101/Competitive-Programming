/*
This was tough at the begining cuz I am not that familiar with java
I still think the code is shit it can be better
 */
package Week3.Easy;

import java.util.ArrayList;
import java.util.List;
import java.io.*;

public class CountingValleys {
    public static int countingValleys(int steps, String path) {
        // Write your code here
        List<Character> valley = new ArrayList<Character>();
        int vallyeCounter = 0;
        boolean STATE = true;
        int size  = path.length();
        int mountainer = 0;
        for (int i =0; i < size; i++){
            if (valley.size() == 0 && path.charAt(i) == 'U'){
                mountainer += 1;
                //System.out.println(mountainer);
            }
            else if (path.charAt(i) == 'D' && mountainer > 0){
                mountainer -= 1;
                //System.out.println("here" + mountainer);
            }
            else if (mountainer == 0 && path.charAt(i) == 'D'){
                valley.add('D');
                //System.out.println("here also" + valley.size());
            }
            else if (valley.size() != 0 && path.charAt(i) == 'U'){
                valley.remove(valley.size()-1);
                //System.out.println("here also" + valley.size());
                STATE = false;
            }
            if (valley.size() == 0 && !STATE){
                vallyeCounter += 1;
                STATE = true;
            }
        }
        return vallyeCounter;
    }
}