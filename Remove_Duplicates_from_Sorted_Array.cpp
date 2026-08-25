#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
    for(auto &value: nums)
    {
        cin >> value;
    }
    int k = 1;
    for (int i = 1; i < n; i++)
    {
         if (nums[i] != nums[i-1])
            {
                nums[k] = nums[i];
                k++;  
            }              
    }
    cout << k; 
}



