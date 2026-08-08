 #include<bits/stdc++.h>
 using namespace std;

 int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
      int target;
    cin >> target; 
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }

    for (int i = 0; i < n; i++){
        for (int j = i + 1; j < n; j++){
        if (nums[i]+nums[j] == target){
            cout << i << endl << j;
        }
        }
 }
    
 }

//its time complexity is O(N^2) if i use a hashmap it can be O(N)



