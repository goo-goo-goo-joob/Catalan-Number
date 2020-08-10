#include<stdio.h>
#include<cstdlib>
#include<cstdio>
#include<locale.h>
#include<stack>
#include <string.h>
using namespace std;
int check(char* br) {
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
	return (i + 1)/ 2;
}
void convert(char* brackets, int* jung1, int* jung2) {
	int j1 = 0, j2 = 0, i = 1;
	while (*brackets != '\0') {
		if (*brackets == '(') {
			jung1[j1] = i;
			j1++;
		}
		else {
			jung2[j2] = i;
			j2++;
		}
		*brackets++;
		i++;
	}
	for (i = 0;i < j1;i++)
		printf("%d ", jung1[i]);
	printf("\n");
	for (i = 0;i < j2;i++)
		printf("%d ", jung2[i]);
}
void print_dot(FILE* f, int* jung1, int* jung2, int n) {
	fprintf(f, "digraph {\n");
	fprintf(f, "		graph[nodesep=\"1\", ranksep=\"50\", resolution=128, frontname=Arial];\n");
	fprintf(f, "		rankdir=LR\n");
	fprintf(f, "		node [frontsize=13.0, shape=plaintext];\n");
	fprintf(f, "Foo [label=<\n");
	fprintf(f, "	<table border=\"0\" cellborder=\"1\" cellspacing=\"0\" cellpadding=\"10\">\n");
	fprintf(f, "	<tr>");
	for (int i = 0; i < n; i++) {
		fprintf(f, "<td>%d</td>", jung1[i]);
	}
	fprintf(f, "</tr>\n");
	fprintf(f, "	<tr>");
	for (int i = 0; i < n; i++) {
		fprintf(f, "<td>%d</td>", jung2[i]);
	}
	fprintf(f, "</tr>\n");
	fprintf(f, "	</table>>];\n");
	fprintf(f, "}\n");
}
int main(int argc, char* argv[]) {
	char command[512];
	int *jung1, *jung2, n;
	strcpy(command, "dot -Tpng jung.dot -o ");
	if (argc == 3)
	{
		strcat(command, argv[2]);
	}
	else
		exit(4);
	setlocale(LC_ALL, "Russian");
	setlocale(LC_NUMERIC, "eng");
	char name[] = "jung.dot";
	FILE* f = fopen(name, "wt");
	if (!f) {
		printf("Error: unable to open file.");
		exit(3);
	}
	n = check(argv[1]);
	jung1 =(int*) malloc(n * sizeof(int));
	jung2 = (int*)malloc(n * sizeof(int));
	convert(argv[1], jung1, jung2);
	print_dot(f, jung1, jung2, n);
	fclose(f);
	system(command);
	free(jung1);
	free(jung2);
	return 0;
}