#include<bits/stdc++.h>
using namespace std;

int main(){
    int maxWealth = 0;
    int m,n;
    cin >> m >> n;
    vector<vector<int>> accounts(m, vector<int>(n));
    for (int i = 0; i < m; i++)
    {
            int wealth = 0;
     for (int j = 0; j < n; j++)
        {
           cin >> accounts[i][j];                
           wealth = wealth + accounts[i][j];
        }
        if(maxWealth < wealth) {
            maxWealth = wealth;
        }
    }
                cout << maxWealth;  
}