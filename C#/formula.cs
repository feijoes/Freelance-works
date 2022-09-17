
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
        
        
        double calcuAla = x + ( ( 7.3*w )/( 9.2*z - x*y ));
        double ala = Math.Pow(2.1*z,calcuAla);
        double abajo = ala - ((z/w)*4.5);
        double arriba = 0.045*x + 2.33*y;
        return (arriba / abajo) * (x*y*z*w);
    }
}