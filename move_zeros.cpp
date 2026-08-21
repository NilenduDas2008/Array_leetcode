#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
    for (auto &value : nums)
    {
        cin >> value;
    }

    int j = 0;
    for (int i = 0; i < n; i++)
    {       
            if (nums[i] != 0)
            {
                swap(nums[i] , nums[j]);
                j++;
            }     
    }

     for (const auto& element : nums) {
        cout << element << '\n';
    }
    


    
}