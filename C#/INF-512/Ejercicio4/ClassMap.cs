public class ClassMap { 
  // member variables
  private int roomNo;
  private string [,] deskArray;
   
 
  //argument constructor
  public ClassMap(int id){
   deskArray = new string[3,4]; 
   roomNo=id;   
  } 
 
  //method to set desk position for student
  public void setDesk(string name) {

    bool flag=false;
    for ( int row=0;row<3;row++){
      for (int col=0;col<4;col++){
      if (deskArray[row,col]==null){
      deskArray[row,col]=name;
      Console.WriteLine(name +"  Desk set at position: Row:"+row +" Column:"+col);
      flag=true;
      break;
     }
    } 
   if (flag==true){
     break;
    } 
   }
   if (flag==false){
  Console.WriteLine("All desks occupied, try another class");
   }
 
  } //end method

  
  //method to diplay the desk map of the class
  public void displayDeskMap(){

    for ( int row=0;row<3;row++){
      for (int col=0;col<4;col++){
        Console.Write("  "+deskArray[row,col]+"  ");   
       }
      Console.WriteLine();
    }
 
  }//end method


  //method to search the desk of a student
  public void searchDesk(string name){

    bool flag=false;
    for ( int row=0;row<3;row++){
      for (int col=0;col<4;col++){
       if (deskArray[row,col] !=null && deskArray[row,col].Equals(name)==true){
         Console.WriteLine(name+"  Desk Position:  Row:  " +row+"  Column:  "+col);
         flag=true;
         break;
        }
      }
   if (flag==true){
     break;
   }
   }
   if (flag==false){ 

   Console.WriteLine("Desk not allocated for:   "+name);
   }
  
  } //end method
}//end class
