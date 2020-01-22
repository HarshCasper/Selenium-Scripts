// https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

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
            long prime=2,max=1;
            while(prime<=n){
                if(n%prime==0){
                    max=prime;
                    n=n/prime;
                }
                else{
                    prime++;
                }
            }
            System.out.println(max);
        }
    }
}

