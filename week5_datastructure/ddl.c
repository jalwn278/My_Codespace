#include <stdio.h>
#include <stdlib.h>

typedef struct dllnode
{
    int number;
    struct dllnode *prev;
    struct dllnode *next;
} dllnode;

// 函数原型：返回新的头指针（以防原链表为空）
dllnode* append(dllnode* head, int val)
{
    // 1. 为新节点分配内存
    dllnode *n = malloc(sizeof(dllnode));
    if (n == NULL)
    {
        return head;
    }

    // 2. 初始化新节点
    n->number = val;
    n->next = NULL; // 既然是最后一个，它的 next 必然是 NULL

    // 3. 特殊情况：如果原链表是空的
    if (head == NULL)
    {
        n->prev = NULL;
        return n; // 新节点即为头节点
    }

    // 4. 寻找当前的尾节点
    dllnode *curr = head;
    while (curr->next != NULL)
    {
        curr = curr->next;
    }

    // 5. 【关键步】建立双向连接
    curr->next = n; // 旧尾巴指向新节点
    n->prev = curr; // 新节点指向旧尾巴

    return head;
}

#include <stdio.h>
#include <stdlib.h>

typedef struct dllnode
{
    int number;
    struct dllnode *prev;
    struct dllnode *next;
} dllnode;

// 截图中的函数原型：dllnode* insert(dllnode* head, VALUE val);
dllnode* insert(dllnode* head, int val)
{
    // a. 为新节点动态分配内存空间
    dllnode *n = malloc(sizeof(dllnode));

    // b. 检查内存是否分配成功（防止内存耗尽）
    if (n == NULL)
    {
        return head; // 或者根据需求处理错误
    }

    // c. 填充新节点的数据，并将其插入到链表开头
    n->number = val;
    n->next = head; // 新节点的下一个指向原来的头
    n->prev = NULL; // 因为新节点是新的头，所以它的前驱必须是 NULL

    // d. 【关键步】修正旧表头节点的 prev 指针
    // 只有当原链表不为空时，原来的头节点才有 prev 需要指向新节点
    if (head != NULL)
    {
        head->prev = n;
    }

    // e. 返回指向新链表头部的指针
    return n;
}
