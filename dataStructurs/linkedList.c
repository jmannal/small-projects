#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

struct node 
{
    int data;
    struct node *next;
};

typedef struct node Node;
//typedef Node *nodePtr;


int main(void)
{
    Node *start = NULL;
    int data;
}


void insert(Node **start, int data)
{
    Node *newNode = (Node*)malloc(sizeof(Node));
    assert(newNode);
}