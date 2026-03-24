#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }
        int l1 = num1.size(),l2 = num2.size();
        vector<int> num(l1+l2,0);
        for (auto i = l1-1;i >= 0;i--) {
            for (auto j = l2-1;j >= 0;j--) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                int sum = num[i+j+1] + mul;
                num[i+j+1] = sum % 10;
                num[i+j] += sum / 10;
            }
        }
        vector<char> ans;
        for (int i = 0;i < l1+l2;i++) {
            if (!(ans.empty()&&num[i] == 0)) {
                ans.push_back(num[i]+'0');
            }
        }
        return ans.empty()?"0":string(ans.begin(),ans.end());
    }
};

int main() {
    Solution solution;
    string num1 = "111",num2 = "123";
    string num = solution.multiply(num1,num2);
    cout << num << endl;
}