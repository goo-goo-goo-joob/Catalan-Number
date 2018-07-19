#include<stdio.h>
#include<cstdlib>
#include<cstdio>
#include<locale.h>
#include<stack>
#pragma warning(disable:4996)
using namespace std;
void check(char* br) {
	int i, j = 0;
	for (i = 0; br[i] != 0;i++) {
		if (br[i] == '(')
			j++;
		else if (br[i] == ')')
			j--;
		else {
			printf("Error: invalid symbol");
			exit(2);
		}
		if (j < 0) {
			printf("Error: incorrect bracket structure");
			exit(1);
		}
	}
	if (j != 0) {
		printf("Error: incorrect bracket structure");
		exit(1);
	}
}
void print_dot_st(FILE* f, char* brackets, int key) {
	stack  <int> st;
	int prev;
	st.push(key++);
	fprintf(f, "	%d;\n", st.top());
	while (*brackets != '\0') {
		if (*brackets == '(') {
			prev = st.top();
			st.push(key++);
			fprintf(f, "	%d--%d;\n", st.top(), prev);
		}
		else
			st.pop();
		brackets++;
	}
}
void print_dot(FILE* f, char* brackets) {
	int key = 1;
	fprintf(f, "graph {\n");
	fprintf(f, "	nodesep=0.6\n");
	fprintf(f, "	rankdir=BT\n");
	fprintf(f, "	node [shape = circle, fontcolor=\"white\"];\n");//fontcolor=\"white\"
	print_dot_st(f, brackets, key);
	fprintf(f, "}\n");
}
int main(int argc, char* argv[]) {
	char command[512];
	strcpy(command, "\"\"%programfiles(x86)%/Graphviz2.38/bin/dot.exe\"\" -Tpng root_tree.dot -o ");
	if (argc == 3)
	{
		strcat(command, argv[2]);
	}
	else
		exit(4);
	setlocale(LC_ALL, "Russian");
	setlocale(LC_NUMERIC, "eng");
	char name[] = "root_tree.dot";
	FILE* f = fopen(name, "wt");
	if (!f) {
		printf("Error: unable to open file.");
		exit(3);
	}
	puts(argv[1]);
	check(argv[1]);
	print_dot(f, argv[1]);
	fclose(f);
	system(command);
	return 0;
}