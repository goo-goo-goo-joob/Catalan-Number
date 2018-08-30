#include"Check.h"

void convert(tnode* tree, char* brackets, int key) {
	tnode *node = tree;
	while (*brackets != '\0') {
		if (*brackets == '(') {
			node->left = (tnode*)malloc(sizeof(tnode));
			tnode *tr_l;
			tr_l = node->left;
			tr_l->left = tr_l->right = NULL;
			tr_l->parent = node;
			tr_l->key = ++key;
			if (*(brackets + 1) == '(')
				node = node->left;
		}
		else if (*brackets == ')') {
			/*char* pos = brackets;
			while (*(pos--) == ')') {
				if(node->parent)
					node = node->parent;
			}
			tnode* pos = node->parent;
			if (!pos->right) {
				node = node->parent;
			}
			else {
				pos = pos->parent;
				while (pos->right&&pos->parent) {
					pos = pos->parent;
				}
				node = pos->left;
			}*/		
			node->right = (tnode*)malloc(sizeof(tnode));
			tnode *tr_r;
			tr_r = node->right;
			tr_r->left = tr_r->right = NULL;
			tr_r->parent = node;
			tr_r->key = ++key;
			if (*(brackets+1) == '(')
				node = node->right;
			else if (*(brackets + 1) == ')') {
				node = node->parent;
				while (node->parent && node->right)
					node = node->parent;
			}
		}
		brackets++;
	}
}
void printTree(FILE* f, tnode* tree) {
	if (tree->left) {
		tnode *tr_l=tree->left;
		fprintf(f, "	%d;\n", tr_l->key);
		fprintf(f, "	%d -- %d;\n", tree->key, tr_l->key);
		printTree(f, tree->left);
	}
	if (tree->right) {
		tnode *tr_r = tree->right;
		fprintf(f, "	%d;\n", tr_r->key);
		fprintf(f, "	%d -- %d;\n", tree->key, tr_r->key);
		printTree(f, tree->right);
	}
}
void print_dot(FILE* f, tnode* tree) {
	fprintf(f, "graph {\n");
	fprintf(f, "	nodesep=0.6\n");
	fprintf(f, "	node [shape = circle, fontcolor=\"white\"];\n");//fontcolor=\"white\"
	fprintf(f, "	%d;\n", tree->key);
	printTree(f, tree);
	fprintf(f, "}\n");
}
void deltree(tnode *tree) {
	if (tree) {
		deltree(tree->right);
		deltree(tree->left);
		free(tree);
	}
}
int  main(int argc, char* argv[]) {

	char command[512];
	strcpy(command, "dot -Tpng tree.dot -o ");
	if (argc == 3)
	{
		strcat(command, argv[2]);
	}
	else
		exit(1);
	setlocale(LC_ALL, "Russian");
	setlocale(LC_NUMERIC, "eng");
	tnode *tree = NULL;
	int key = 1;
	char name[] = "tree.dot";
	FILE* f=fopen(name, "wt");
	if (!f) {
		printf("Error: unable to open file.");
		exit(3);
	}
	tree = (tnode*)malloc(sizeof(tnode));
	tree->left = tree->right = NULL;
	tree->key = key;
	tree->parent = NULL;
	puts(argv[1]);
	check(argv[1]);
	convert(tree, argv[1], key);
	print_dot(f, tree);
	deltree(tree);
	tree = NULL;
	fclose(f);
	system(command);
	return 0;
}