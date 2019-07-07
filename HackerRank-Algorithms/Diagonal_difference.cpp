//https://hackerrank-challenge-pdfs.s3.amazonaws.com/8662-diagonal-difference-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562476807&Signature=rQG2omvtoU5cOMq6HaTYQ5lRv40%3D&response-content-disposition=inline%3B%20filename%3Ddiagonal-difference-English.pdf&response-content-type=application%2Fpdf
#include <bits/stdc++.h>

using namespace std;

// Complete the diagonalDifference function below.
int diagonalDifference(vector<vector<int>> arr,int n)
{
    int sum1=0,sum2=0;
    for(int i=0; i<n ;i++)
    {
        for(int j=0; j<n ;j++)
        {
            if(i==j)
                sum1+=arr[i][j];
            if((i+j)==(n-1))
                sum2+=arr[i][j];
        }
    }
    return abs(sum1-sum2);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i].resize(n);

        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = diagonalDifference(arr,n);

    fout << result << "\n";

    fout.close();

    return 0;
}
