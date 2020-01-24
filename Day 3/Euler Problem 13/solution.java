// https://www.hackerrank.com/contests/projecteuler/challenges/euler013/problem

import java.io.*;
import java.util.*;
import java.math.BigInteger;  

public class Solution {

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        s.nextLine();
        BigInteger sum=new BigInteger("0");
        String number;
        for(int i=0;i<n;i++){
            number=s.nextLine();
            BigInteger temp=new BigInteger(number);
            sum=sum.add(temp);

        }
        String final_answer=sum+"";
        System.out.println(final_answer.substring(0,10));
    }
}

