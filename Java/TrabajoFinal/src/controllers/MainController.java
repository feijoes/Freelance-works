package controllers;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class MainController {



    MainController(){

    }

    public static void saveinfo(Map<String,String> info) throws IOException {
        FileWriter fw = null;
        BufferedWriter bw = null;
        PrintWriter pw = null;
        try {

            fw = new FileWriter("names.txt", true);
            bw = new BufferedWriter(fw); pw = new PrintWriter(bw);
            int points = 0;
            for (Map.Entry<String, String> entry : info.entrySet()) {
                if (entry.getKey().equals("AntecedentesFamiliares"))
                {
                  if(!(entry.getValue().isEmpty()))  {
                      points++;
                  }
                } else if (entry.getKey().equals("Fiebre")) {
                    int num = 0;
                    try {
                       num = Integer.parseInt(entry.getValue());
                    }catch (NumberFormatException e ){
                    }

                    if (num > 38)
                    {
                        points++;
                    }
                } else if (entry.getKey().equals("satu")) {
                    int num = 0;
                    try {
                        num = Integer.parseInt(entry.getValue());
                    }catch (NumberFormatException e ){
                    }

                    if (num > 90)
                    {
                        points++;
                    }

                } else {
                    if (!entry.getValue().equals("no"))
                    {
                        points++;
                    }
                }

            }

            String s = "";
            System.out.println("Data Successfully appended into file");
            if(points <=2){
                s = "casa";
            }
            else if( points <=4){
                s = "observacion";
            }
            else if (points <=6){
                s = "hospitalizacion";
            }
            else if (points > 6){
                s = "uci";

            }
            System.out.println(points);
            pw.println(s);
            pw.flush();
        } finally {
            try {
                pw.close(); bw.close(); fw.close();
            } catch (IOException io) {
                // can't do anything
                }}}



    public static  ArrayList<Integer> getInfo() throws IOException {
        File file = new File(
                "names.txt");

        int casa = 0;
        int hospitalizacion =0;
        int observacion = 0;
        int uci = 0;
        BufferedReader br
                = new BufferedReader(new FileReader(file));

        // Declaring a string variable
        String st;
        // Condition holds true till
        // there is character in a string
        while ((st = br.readLine()) != null){

            if(st.toString() .equals( "casa")){
                casa++;
            }
            if(st.toString().equals( "observacion")){
                hospitalizacion++;
            }if(st.toString().equals( "hospitalizacion")){
                uci++;
            }if(st.toString().equals( "uci")){
                observacion++;
            }

        }
        ArrayList<Integer> nums = new ArrayList<Integer>();
        nums.add(casa);
        nums.add(observacion);
        nums.add(hospitalizacion);
        nums.add(uci);
        return nums;
    }
}
