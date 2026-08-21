#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    unordered_set<int> s(nums.begin(), nums.end());
    if(s.size() == n){
        cout << "false";
    }
    else {
           cout << "true";
    }
    
}


//in this problem i dont need to use set(t.c-->O(logn)) (i dont need sorted array i need just duplicate) so i use unordered set(t.c--> O(1))