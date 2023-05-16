// Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, 
// какое число большее, а какое меньшее.

// a = 5; b = 7 -> max = 7
// a = 2 b = 10 -> max = 10
// a = -9 b = -3 -> max = -3
//Бабаян Р.А.
using System;

Console.Write("Введите 1-ое число:");
int num1 = int.Parse(Console.ReadLine());
Console.Write("Введите 2-ое число:");
int num2 = int.Parse(Console.ReadLine());
int min = Math.Min(num1,num2);
int max = Math.Max(num1,num2);
Console.WriteLine($"Max={max}");
Console.WriteLine($"Min={min}");
