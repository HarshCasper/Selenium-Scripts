// https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

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
            int result=-1;
            for(int i=1;i<=n/3;i++){
                int c=((i*i)/(2*n-2*i))+(n/2)-(i/2);
                int b = n - i - c;

                if (i * i + b * b == c * c && i < b && b < c) {
                    result = i * b * c;
                }
            }
            System.out.println(result);
            }
            
        }
    }


