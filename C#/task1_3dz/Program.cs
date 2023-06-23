//Задача 1. Найти среднее арифметическое среди всех элементов массива [2, 5, 13, 7, 6, 4] с помощью блок-схемы

double sum = 0;
int index = 0;
int size = 6;
int [] numbers = new int[6] {2, 5, 13, 7, 6, 4};
while (index < size)
{
    sum = sum + numbers[index];
    index = index + 1;
}
double avg = sum / size;
Console.Write($"Cреднее арифметическое массива: {System.Math.Round(avg,3)}");
