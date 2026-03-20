#include<bits/stdc++.h>
class Solution {
public:
    // 牛顿迭代公式 xi+1 = 1/2 * (xi + C/xi)
    int mySqrt(int x) {
       if (x == 0) {
            return 0;
       }
       double x0 = x,C = x;
       while (1) {
            double xi = 0.5 * (x0 + C/x0);
            if (fabs(x0 - xi) <= 1e-7) {
                break;
            }
            x0 = xi;
       }
       return int(x0);
    }
};