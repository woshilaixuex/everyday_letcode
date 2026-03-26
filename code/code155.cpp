#include<bits/stdc++.h>
using namespace std;
class MinStack {
    stack<int> xstack;
    stack<int> mstack;
public:
    MinStack() {
        mstack.push(INT_MAX);
    }
    
    void push(int val) {
        xstack.push(val);
        mstack.push(min(mstack.top(),val));
    }
    
    void pop() {
        xstack.pop();
        mstack.pop();
    }
    
    int top() {
        return xstack.top();
    }
    
    int getMin() {
        return mstack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */