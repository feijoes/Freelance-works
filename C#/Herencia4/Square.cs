using System;
namespace Herencia4
{
    public class Square : Rectangle
    {
        public Square(): base()
        {
        }
        public Square(double side): base(side,side)
        {   
        }
        public Square(double side,string color, bool filled): base(side,side,color,filled)
        {
        }
        public void setSide(double side)
        {
            base.setLength(side);
            base.setWidth(side);
        }
        public double getSide()
        {
            return base.getLength();
        }
        public override void setWidth(double side)
        {
            base.setLength(side);
            base.setWidth(side);
        }
        public override void setLength(double side)
        {
            base.setLength(side);
            base.setWidth(side);
        }

        public override string toString()
        {
            return $"A Square with side={this.getSide()}, which is a subclass of {base.toString()}";
        }
    }    
}