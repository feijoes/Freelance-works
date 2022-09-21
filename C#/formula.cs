
using System;

public class Formula
{
    public static void Main(string[] args)
    {
        double x,y,z,w;
        Console.WriteLine("Enter x:");
        x = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Enter y:");
        y = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Enter z:");
        z = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Enter w:");
        w = Convert.ToDouble(Console.ReadLine());
        
        Console.WriteLine(Calcular(x,y,z,w));
    }
    
    public static double Calcular(double x,double y,double z,double w){

        return (((x*0.045)+(2.33*y))/(Math.Pow(2.1*z,(x+((7.3*w)/(9.2*z-(x*y)))))-(4.5*z/w))*z*y*z*w);
    }
}


