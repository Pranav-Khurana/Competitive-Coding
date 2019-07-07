//https://hackerrank-challenge-pdfs.s3.amazonaws.com/13689-java-if-else-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562480240&Signature=uYwreBXpH1N2EjDgPzsGm55b0b8%3D&response-content-disposition=inline%3B%20filename%3Djava-if-else-English.pdf&response-content-type=application%2Fpdf
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        if(N%2!=0 || (N>=6 && N<=20) )
            System.out.println("Weird");
        else
            System.out.println("Not Weird");

        scanner.close();
    }
}
