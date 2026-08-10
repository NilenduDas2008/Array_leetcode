 #include<bits/stdc++.h>
 using namespace std;

 int main(){
    int answer = -1;
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    
    for(int i = 0; i < n; i++) {
        int left_sum = 0;
        int right_sum = 0;
        
    for(int j = 0; j < i; j++){
        left_sum = left_sum + nums[j];
    }

    for(int k = n-1; k > i; k--){
        right_sum = right_sum + nums[k];
    }
    
    if(left_sum == right_sum){
        answer =  i;
     break;
    }
}
cout <<  answer;
}

 
 
 
 
 