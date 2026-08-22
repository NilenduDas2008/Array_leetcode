
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> prices(n);

    for (auto &value : prices) {
        cin >> value;
    }

    int purchasing_price = prices[0];
    int maxProfit = 0;

    for (int i = 1; i < n; i++) {
        int currentProfit = prices[i] - purchasing_price;

        if (currentProfit > maxProfit) {
            maxProfit = currentProfit;
        }

        if (prices[i] < purchasing_price) {
            purchasing_price = prices[i];
        }
    }

    cout << maxProfit;

    return 0;
}