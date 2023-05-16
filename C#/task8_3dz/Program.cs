/*
Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.

14212 -> нет

12821 -> да

23432 -> да
*/

bool IsPalindrom(int num)
{
    if ((num / 10000 == num % 10) && (num / 1000 % 10 == num / 10 % 10))
    {
        Console.WriteLine("Это палиндром");
        return true;
    }

    Console.WriteLine("Это не палиндром");
    return false;
}


Console.WriteLine("Введите пятизначное число:");
int number = int.Parse(Console.ReadLine());
if (number < 10000 || number > 99999)
{
    Console.WriteLine("Это не пятизначное число:");
}
IsPalindrom(number);
