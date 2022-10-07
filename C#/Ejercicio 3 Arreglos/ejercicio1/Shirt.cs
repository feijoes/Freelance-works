using System;
public class Shirt {

  public int shirtID = 0; // Default ID for the shirt
  public String description = "-description required-"; // default
  
  // The color codes are R=Red, B=Blue, G=Green, U=Unset
  public char colorCode = '\u0000';
  public double price = 0.0; // Default price for all shirts
  public int quantityInStock = 0; // Default quantity for all shirts
  
  Shirt() {  }

    Shirt(int ID, String d, char c, double p, int q) 
	{
		shirtID = ID;
		description = d;
		colorCode = c;
		price = p;
		quantityInStock = q;
    }

  // This method displays the values for an item
  public void displayInformation() {
    Console.WriteLine("******SHIRT INFORMATION******");
    Console.WriteLine("Shirt ID: {0}" , shirtID);
    Console.WriteLine("Shirt description: {0}" , description);
    Console.WriteLine("Color Code: {0}" , colorCode);
    Console.WriteLine("Shirt price: {0}",  price);
    Console.WriteLine("Quantity in stock:{0} " , quantityInStock);
    Console.WriteLine("*****************************");

  } // end of display method
} // end of class



