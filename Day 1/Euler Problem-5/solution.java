// https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class Solution {
    public static int gcd(int a,int b){
        if(b==0){
            return a;
        }
        return gcd(b,a%b);
    }
    public static int lcm(int a,int b){
        return (a*b)/gcd(a,b);
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int LCM=1;
            for(int i=2;i<=n;i++){
                LCM=lcm(LCM,i);
            }
            System.out.println(LCM);
        }
    }
}

