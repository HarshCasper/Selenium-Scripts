// https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem

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
            int k = in.nextInt();
            String num = in.next();
            int product=1;
            int max=0;
            int i,j;
            for(i=0;i<n-k;i++){
                for(j=0;j<k;j++){
                    char ch=num.charAt(i+j);
                    int m=Integer.parseInt(String.valueOf(ch));
                    product=product*m;
                }
                if(product>=max){
                    max=product;
                }
                product=1;

            }
            System.out.println(max);
        }
    }
}

