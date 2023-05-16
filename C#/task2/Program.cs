//Задача 4: Напишите программу, которая принимает на вход три числа 
//и выдаёт максимальное из этих чисел.

//2, 3, 7 -> 7
//44 5 78 -> 78
//22 3 9 -> 22
//Бабаян Р.А.

using System;

Console.Write("Введите 1-ое число:");
int num1 = int.Parse(Console.ReadLine());
Console.Write("Введите 2-ое число:");
int num2 = int.Parse(Console.ReadLine());
Console.Write("Введите 3-ье число:");
int num3 = int.Parse(Console.ReadLine());

int max_2 = Math.Max(num1,num2);
int max = Math.Max(max_2, num3);
Console.WriteLine($"Max={max}");

