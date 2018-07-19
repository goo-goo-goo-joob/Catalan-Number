#pragma once
typedef struct {
	int key;
	struct tnode *left, *right, *parent;
} tnode;