//Задача 8: Напишите программу, которая на вход принимает число (N), 
//а на выходе показывает все чётные числа от 1 до N.

//5 -> 2, 4
//8 -> 2, 4, 6, 8

using System;

Console.Write("Введите число:");
int num = int.Parse(Console.ReadLine());
int[] a=new int[num+1];
for(int i=1;i<=num;i++)
{
    a[i] = i;
    if (a[i] % 2==0)
    {
        Console.Write($"{a[i]} ");
    }

}
