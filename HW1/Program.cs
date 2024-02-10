using System;
using System.Text.RegularExpressions;

class Program
{
    static void Main(string[] args)
    {
        while (true)
        {
            Console.Write("Enter input (for exit press 0) :");
            string input = Console.ReadLine();
            if (input == "0") 
            {
                break;
            }
            if (IsEmail(input))
            {
                Console.WriteLine("It's an email.");
            }
            else if (IsMathExpression(input))
            {
                Console.WriteLine("It's a mathematical expression.");
            }
            else if (IsURL(input))
            {
                Console.WriteLine("It's a URL.");
            }
            else if (IsPostalCode(input))
            {
                Console.WriteLine("It's a postal code.");
            }
            else if (IsPhoneNumber(input))
            {
                Console.WriteLine("It's a phone number.");
            }
            else
            {
                Console.WriteLine("Type not recognized.");
            }
        }
    }

    static bool IsEmail(string input)
    {
        string emailPattern = @"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b";
        return Regex.IsMatch(input, emailPattern);
    }

    static bool IsMathExpression(string input)
    {
        string mathPattern = @"\b\d+(\s*[\+\-\*\/]\s*\d+)+\b";
        return Regex.IsMatch(input, mathPattern);
    }

    static bool IsURL(string input)
    {
        //string urlPattern = @"(https?|ftp)://[^\s/$.?#].[^\s]*";
        string urlPattern = @"^(https?://|www\.)[^\s/$.?#].[^\s]*"; ;

        return Regex.IsMatch(input, urlPattern);
    }

    static bool IsPostalCode(string input)
    {
        string postalCodePattern = @"\b\d{10}\b";
        return Regex.IsMatch(input, postalCodePattern);
    }

    static bool IsPhoneNumber(string input)
    {
        string phonePattern = @"\+98\d{9}";
        return Regex.IsMatch(input, phonePattern);
    }

}
