using System;
namespace Herencia4
{
    public class Circle : Shape
    {
        double radius;
        public Circle(): base()
        {
            this.radius = 1.0;   
        }
        public Circle(double radius): base()
        {
            this.radius = radius;   
        }
        public Circle(double radius,string color, bool filled): base(color,filled)
        {
          this.radius = radius;
        }
        public double getRadius()
        {
            return this.radius;
        }
        public void setRadius(double radius)
        {
            this.radius = radius;
        }
        public double getArea()
        {
            return Math.PI * radius * radius;
        }
        public double getPerimeter()
        {
            return 2 * Math.PI * radius;
        }
        public override string toString()
        {
            return $"A Circle with radius={radius}, which is a subclass of {base.toString()},]";
        }
    }    
}