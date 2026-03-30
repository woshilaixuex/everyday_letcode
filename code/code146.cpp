#include <bits/stdc++.h>
using namespace std;
class LinkNode{
public:
    int key;
    int val;
    LinkNode* next;
    LinkNode* prev;
    LinkNode(int key=-1,int val=-1,LinkNode* next=nullptr,LinkNode* prev=nullptr):key(key),val(val),next(next),prev(prev){};
};
class LRUCache {
public:
    LinkNode* head;
    LinkNode* tail;
    unordered_map<int,LinkNode*> node_map;
    int len;
    int cap;
    LRUCache(int capacity) {
        head = new LinkNode();
        tail = new LinkNode();
        head->next = tail;
        tail->prev = head;
        len = 0;
        cap = capacity;
    }
    
    int get(int key) {
        if (!node_map.count(key)) return -1;
        LinkNode* node = node_map[key];
        removeNode(node);
        addToHead(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (node_map.count(key)) {
            LinkNode* del = node_map[key];
            removeNode(del);
            node_map.erase(key);
            --len;
        }
        if (len >= cap) {
            LinkNode* del = tail->prev;
            removeNode(del);
            node_map.erase(del->key);
            --len; 
        }
        ++len;
        LinkNode* node = new LinkNode(key,value,nullptr,nullptr);
        addToHead(node);
        node_map[key] = node;
    }
    void removeNode(LinkNode* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void addToHead(LinkNode* node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
int main() {
    LRUCache lrucahce(2);
    lrucahce.put(1,1);
    lrucahce.put(2,2);
    lrucahce.get(1);
    lrucahce.put(3,3);
    lrucahce.get(2);
    lrucahce.put(4,4);
    lrucahce.get(1);
    lrucahce.get(3);
    lrucahce.get(4);
}