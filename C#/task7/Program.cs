/*
int Prompt(string message)
{
    System.Console.Write(message);
    string value = Console.ReadLine();
    int result = Convert.ToInt32(value);
    return result;
}
*/

int Prompt(string message)
{
    System.Console.Write(message);
    string value = Console.ReadLine();
    int result = Convert.ToInt32(value);
    return result;
}

bool IsWeekend(int day)
{
    if (day > 5)
    {
        return true;
    }
    return false;
}


bool ValidateDay(int number)
{
    if (number > 0 && number <=7)
    {
        return true;
    }
    Console.WriteLine("Это не день недели");
    return false;
}

int day = Prompt ("Введите день недели:");
if (ValidateDay(day))
{
    if (IsWeekend(day))
    {
        Console.WriteLine("Это выходной");
    }
    else
    {
        Console.WriteLine("Это будний день");
    }
}