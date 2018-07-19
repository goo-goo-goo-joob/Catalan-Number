#include"Check.h"
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