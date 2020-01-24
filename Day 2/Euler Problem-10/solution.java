// https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static boolean checkPrime(long n){
    if(n<2) return false;
    if(n==2) return true;
    else{
        for(int i=2;i<=Math.pow(n,0.5)+1;i++){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }

}

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int sum=0;
            for(int j=1;j<=n;j++){
                if(checkPrime(j)){
                    sum=sum+j;
                }

            }
            System.out.println(sum);
        }
    }
}

