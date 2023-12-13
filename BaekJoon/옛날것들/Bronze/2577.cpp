// https://www.acmicpc.net/problem/2577
#include <stdio.h>

int main()
{
int a, b, c;
int total, rest;
int i;
int m[10] = {};

scanf("%d", &a);
scanf("%d", &b);
scanf("%d", &c);

total = a * b * c;

while (total > 0)
{
rest = total % 10;
total = total / 10;
m[rest]++;
}
for (i = 0; i < 10; i++)
{
printf("%d\n", m[i]);
}
}