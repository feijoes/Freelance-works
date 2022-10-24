using System;
namespace Herencia4
{
    public class Rectangle : Shape
    {
        double width;
        double length;
        public Rectangle(): base()
        {
            this.width = 1.0;
            this.length = 1.0;   
        }
        public Rectangle(double width,double length): base()
        {
            this.width = width;
            this.length = length;   
        }
        public Rectangle(double length,double width,string color, bool filled): base(color,filled)
        {
          this.width = width;
          this.length =length;
        }
        public double getWidth()
        {
            return this.width;
        }
        public virtual void setWidth(double width)
        {
            this.width = width;
        }
        public double getLength()
        {
            return this.length;
        }
        public virtual void setLength(double length)
        {
            this.length = length;
        }

        public double getArea()
        {
            return width * length;
        }
        public double getPerimeter()
        {
            return  2 * (length + width);
        }
        public override string toString()
        {
            return $"A Rectangle with width={width} and length={this.length}, which is a subclass of {base.toString()}";
        }
    }    
}