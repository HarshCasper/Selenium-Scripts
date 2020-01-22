// https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int sum=0;
            for(int i=1;i<n;i++){
                if(i%3==0 || i%5==0){
                    sum+=i;
                }
            }
            System.out.println(sum);
        }
    }
}

