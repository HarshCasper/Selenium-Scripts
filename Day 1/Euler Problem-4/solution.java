// https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem

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
            int product=0,value=0;
            for(int i=100;i<=999;i++){
                for(int j=100;j<=999;j++){
                    product=i*j;
                    int num=product;
                    int reverse_number=0;
                    while(num!=0){
                        reverse_number=reverse_number*10;
                        reverse_number=reverse_number+(num%10);
                        num=num/10;
                    }
                    if(product==reverse_number && product<n){
                        if(product>value){
                            value=product;
                        }
                    }
                }
            }
            System.out.println(value);
        }
    }
}

