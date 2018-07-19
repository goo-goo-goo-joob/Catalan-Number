#include<stdio.h>
#include<cstdlib>
#include<cstdio>
#include<locale.h>
#include<stack>
using namespace std;
void check(char* br) {
	int i, j = 0;
	for (i = 0; br[i] != 0;i++) {
		if (br[i] == '(')
			j++;
		else if (br[i] == ')')
			j--;
		else {
			printf("Oшибка: неверный символ");
			exit(1);
		}
		if (j < 0) {
			printf("Oшибка: неправильная скобочная структура");
			exit(1);
		}
	}
	if (j != 0) {
		printf("Ошибка: неправильная скобочная структура");
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
	fprintf(f, "	node [shape = circle];\n");//fontcolor=\"white\"
	print_dot_st(f, brackets, key);
	fprintf(f, "}\n");
}
int main() {
	char brackets[] = "()";//(()())()()()(())
	setlocale(LC_ALL, "Russian");
	setlocale(LC_NUMERIC, "eng");
	char name[] = "root_tree.dot";
	FILE* f = fopen(name, "wt");
	if (!f) {
		printf("Ошибка: невозможно открыть файл.");
		exit(1);
	}
	puts(brackets);
	check(brackets);
	print_dot(f, brackets);
	fclose(f);
	system("dot -Tpng root_tree.dot -o ~/root_tree.png");
	return 0;
}