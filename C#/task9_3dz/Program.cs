/*
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.

A (3,6,8); B (2,1,-7), -> 15.84

A (7,-5, 0); B (1,-1,9) -> 11.53
*/

using System;


Console.WriteLine("Введите координаты точки А(х,у,z):");
Console.Write("А(х):");
double ax = double.Parse(Console.ReadLine());
Console.Write("А(y):");
double ay = double.Parse(Console.ReadLine());
Console.Write("А(z):");
double az = double.Parse(Console.ReadLine());

Console.WriteLine("Введите координаты точки B(х,у,z):");
Console.Write("B(х):");
double bx = double.Parse(Console.ReadLine());
Console.Write("B(y):");
double by = double.Parse(Console.ReadLine());
Console.Write("B(z):");
double bz = double.Parse(Console.ReadLine());

double result = Math.Sqrt(Math.Pow((bx-ax),2)+Math.Pow((by-ay),2)+Math.Pow((bz-az),2));
Console.WriteLine($"Расстояние:{result}");

