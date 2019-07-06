//https://hackerrank-challenge-pdfs.s3.amazonaws.com/23074-birthday-cake-candles-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1562405974&Signature=Qgg2jz%2B%2BNBhwr2tgq3ouzsZDsB0%3D&response-content-disposition=inline%3B%20filename%3Dbirthday-cake-candles-English.pdf&response-content-type=application%2Fpdf
#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the birthdayCakeCandles function below.
int birthdayCakeCandles(vector<int> arr,int n)
{
    int m=0,i,c=0;
    for(i=0; i<n; i++)
        m=m>arr[i]?m:arr[i];
    for(i=0; i<n; i++)
        if(arr[i]==m)
           c++;
    return c;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int ar_count;
    cin >> ar_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string ar_temp_temp;
    getline(cin, ar_temp_temp);

    vector<string> ar_temp = split_string(ar_temp_temp);

    vector<int> ar(ar_count);

    for (int i = 0; i < ar_count; i++) {
        int ar_item = stoi(ar_temp[i]);

        ar[i] = ar_item;
    }

    int result = birthdayCakeCandles(ar,ar_count);

    fout << result << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
