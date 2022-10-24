namespace Herencia4
{
    public class Shape
    {
        string color;
        bool filled;
        public Shape()
        {
            this.color ="red";
            this.filled = true;
        }
        public Shape(string color, bool filled)
        {
            this.color = color;
            this.filled =filled;
        }
        public string getColor()
        {
            return this.color;
        }
        public void setColor(string newcolor)
        {
            this.color = newcolor;
        }
        public bool isFilled()
        {
            return this.filled;
        }
        public void setFilled(bool filled)
        {
            this.filled =filled;
        }
        public virtual string toString()
        {
            if (filled)
            {
                return $"A Shape with color of {this.color} and filled]";
            }
            else
            {
                return $"A Shape with color of {this.color} and Not filled";
            }
            
        }
    }    
}