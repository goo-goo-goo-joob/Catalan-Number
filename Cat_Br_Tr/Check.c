#include"Check.h"
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
			printf("Oшибка: неправильна¤ скобочна¤ структура");
			exit(1);
		}
	}
	if (j != 0) {
		printf("ќшибка: неправильна¤ скобочна¤ структура");
		exit(1);
	}
}