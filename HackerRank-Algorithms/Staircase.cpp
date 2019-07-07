//https://hackerrank-challenge-pdfs.s3.amazonaws.com/8636-staircase-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562477793&Signature=1Cp5782C1TFhALHaPapck%2B8kDo4%3D&response-content-disposition=inline%3B%20filename%3Dstaircase-English.pdf&response-content-type=application%2Fpdf
#include <bits/stdc++.h>

using namespace std;

// Complete the staircase function below.
void staircase(int n)
{
    for(int i=0; i<n; i++)
    {
        for(int j=i; j<n-1; j++)
            cout<<" ";
        for(int k=0; k<=i; k++)
            cout<<"#";
        cout<<"\n";
    }
}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
