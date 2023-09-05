/*Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк, 
длина которых меньше, либо равна 3 символам. Первоначальный массив можно ввести с клавиатуры, 
либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями, 
лучше обойтись исключительно массивами.

Примеры:
[“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
[“1234”, “1567”, “-2”, “computer science”] → [“-2”]
[“Russia”, “Denmark”, “Kazan”] → []

*/
void PrintArray (string[] array)
{

    for (int k = 0; k < array.GetLength(0); k++)
    {
        Console.Write(array[k]+ " ");
    }
}

void NewArray (string[] array1, string[] array2)
{
    int j = 0;
    for (int i = 0; i < array1.GetLength(0); i++)
    {   
        if (array1[i].Length <= 3)
        {
            array2[j] = array1[i];
            j++;
        }    
    }
}

string[] a = {"Hello", "2", "world", ":-)"};
string[] b = new string[a.GetLength(0)];
NewArray(a,b);
PrintArray(b);
