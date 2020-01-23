// https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static boolean isPrime(long n){
    if(n<2) return false;
    else if(n==2) return true;
    for(int i=2;i<Math.pow(n,0.5)+1;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;   
}
    public static long nthprime(long n){
    long numberOfPrimes=0;
    long prime=1;
    while(numberOfPrimes<n){
        prime++;
        if(isPrime(prime)){
            numberOfPrimes++;

        }
    }
    return prime;
}

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            long n = in.nextInt();
            System.out.println(nthprime(n));

        }
    }
}

