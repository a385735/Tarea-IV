#include <stdio.h>

int main ()
{
int a, b, i, fibo, ne;

printf("Ingrese cuantos numeros de la serie fibonacci quisiera obtener: ");
scanf("%d", &fibo);
printf("0");

a = 1;
b = 0;

  for (i = 1; i < fibo; i++) { 
	ne = a + b;
            printf(ne);
            a = b;
            b = ne;

}
}