#include"Check.h"
void check(char* br) {
	int i, j = 0;
	for (i = 0; br[i] != 0;i++) {
		if (br[i] == '(')
			j++;
		else if (br[i] == ')')
			j--;
		else {
			printf("O�����: �������� ������");
			exit(1);
		}
		if (j < 0) {
			printf("O�����: ����������� �������� ���������");
			exit(1);
		}
	}
	if (j != 0) {
		printf("������: ����������� �������� ���������");
		exit(1);
	}
}