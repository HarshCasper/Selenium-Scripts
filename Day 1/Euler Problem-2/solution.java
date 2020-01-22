// https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

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
            long n = in.nextLong();
            long f1=1,f2=2,f=0,sum=0;
            while(f1<n){
                if(f1%2==0){
                    sum+=f1;
                }
                f=f1+f2;
                f1=f2;
                f2=f;
            }
            System.out.println(sum);
            
        }
    }
}

