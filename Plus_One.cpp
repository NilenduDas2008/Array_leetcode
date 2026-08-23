#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    vector<int> digits(n);
    for (auto &value : digits)
    {
        cin >> value;
    }
    int i ;
    for ( i = n-1; i >= 0; i--)
    {
        if (digits[i] == 9)
        {
            digits[i] = 0;
        }
         else {
                digits[i] += 1;
                break;
         }
        
    }

    if (i == -1)
    {
        digits.insert(digits.begin(), 1);
    }
    
    for (auto it = digits.begin(); it != digits.end(); ++it) {
    cout << *it << " ";
}

    
}