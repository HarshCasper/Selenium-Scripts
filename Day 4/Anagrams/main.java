import java.io.*; 
import java.util.Arrays; 
import java.util.Collections; 
import java.util.Scanner;

public class main{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        String word1=s.nextLine();
        String word2=s.nextLine();
        char[] ch1 = word1.toCharArray(); 
        char[] ch2 = word2.toCharArray(); 
        if(ch1.length!=ch2.length){
            System.out.println("They are not Anagrams");
        }
        else{
            Arrays.sort(ch1);
            Arrays.sort(ch2);
            for(int i=0;i<ch1.length;i++){
                if(ch1[i]!=ch2[i]){
                    System.out.println("They are not Anagrams");
                    break;
                }
            }
            System.out.println("They are Anagrams");
        }
    }
}
    
