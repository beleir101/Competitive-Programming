package Week1;
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
public class HR_Grading_Students {

        public static List<Integer> gradingStudents(List<Integer> grades){
            List<Integer> graded = new ArrayList<Integer>();
            for(int i : grades){
                if (i < 38){
                    graded.add(i);
                }
                else{
                    int k = i / 5;
                    int p = 5 * (k+1);
                    if (p - i < 3){
                        graded.add(p);
                    }
                    else{
                        graded.add(i);
                    }
                }
            }

            return graded;
        }

}
