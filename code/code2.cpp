#include<bits/stdc++.h>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dump = new ListNode(-1,nullptr);
        ListNode* curr = dump;

        int dx = 0;
        while (l1 && l2) {
            int val = (l1->val + l2->val + dx) % 10;
            dx = (l1->val + l2->val + dx) / 10;
            curr->next = new ListNode(val,nullptr);
            curr = curr->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        ListNode* node = nullptr;
        if (l1 or l2) {
            node = l1? l1:l2;
        }
        while (dx != 0 or node) {
            if (node) {
                int val = (node->val + dx) % 10;
                dx = (node->val + dx) / 10;
                curr->next = new ListNode(val,nullptr);
                curr = curr->next;
                node = node->next;
            }else {
                int val = dx;
                dx = 0;
                curr->next = new ListNode(val,nullptr);
            }
        }
        return dump->next;
    }
};
int main() {
    Solution solution;
    ListNode* l1 = new ListNode(0);
    ListNode* l2 = new ListNode(1,new ListNode(8));
    ListNode* l = solution.addTwoNumbers(l1,l2);
    while (l) {
        cout << l->val << " ";
        l = l->next;
    }
}