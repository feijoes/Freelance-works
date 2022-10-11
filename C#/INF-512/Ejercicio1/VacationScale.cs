public class VacationScale {

    int [] vacationDays;
 
    
    public void setVacationScale (){
    vacationDays = new int[10];
    vacationDays[0] = 10;
    vacationDays[1] = 15;
    vacationDays[2] = 15;
    vacationDays[3] = 15;
    vacationDays[4] = 20;
    vacationDays[5] = 20;
    vacationDays[6] = 25;
    vacationDays[7] = 25;
    vacationDays[8] = 30;
    vacationDays[9] = 30;
    }
    
     public void displayVacationDays (int yearsOfService){
     if (yearsOfService < 0) {
     Console.WriteLine("Numero de anys invalid");
     } else if (yearsOfService <= 6){
         Console.WriteLine("Dies de vacacions: " + vacationDays[yearsOfService]);
     } else {
         Console.WriteLine("Dies de vacacions: " + vacationDays[8]);
     }
   }   
}