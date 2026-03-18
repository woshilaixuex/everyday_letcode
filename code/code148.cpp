/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    ListNode* sortList(ListNode* head) {
        if (head == nullptr) {
            return head;
        }

        int lenght = 0;
        ListNode* node = head;
        while (node) {
            node = node->next;
            lenght++;
        }
        ListNode* dump = new ListNode(-1,head);
        for (int mergeLen = 1;mergeLen < lenght;mergeLen *= 2) {
            ListNode* prev = dump;
            ListNode* curr = dump->next;
            while (curr){
                ListNode* l1 = curr;
                for (int i = 1;i < mergeLen && curr->next != nullptr;i++) {
                    curr = curr->next;
                }
                ListNode* l2 = curr->next;
                curr->next = nullptr;
                curr = l2;
                for (int i = 1;i < mergeLen && curr != nullptr && curr->next != nullptr;i++) {
                    curr = curr->next;
                }
                ListNode* next = nullptr;
                if (curr != nullptr) {
                    next = curr->next;
                    curr->next = nullptr;
                }
                ListNode* ml = mergeList(l1,l2);
                prev->next = ml;
                while (prev->next) {
                    prev = prev->next;
                } 
                curr = next;
            }
        }
        return dump->next;
    }
    ListNode* mergeList(ListNode* l1,ListNode* l2) {
        ListNode* dump = new ListNode(-1);
        ListNode* temp = dump, *temp1 = l1, *temp2 = l2;
        while (temp1 && temp2) {
            if (temp1->val <= temp2->val) {
                temp->next = temp1;
                temp1 = temp1->next;
            }else {
                temp->next = temp2;
                temp2 = temp2->next;
            }
            temp = temp->next;
        }
        if (temp1) {
            temp->next = temp1;
        }
        if (temp2) {
            temp->next = temp2;
        }
        return dump->next;
    }
};
int main(){
    ListNode* head = new ListNode(4,new ListNode(2,new ListNode(1,new ListNode(3,new ListNode(5)))));
    Solution* s = new Solution();
    ListNode* ans = s->sortList(head);
    cout << " " << endl;
}