import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.FileWriter;
import java.io.IOException;

public class Fail2Ban
{
    public static void main(String[] args) 
    {
        //2 arrays to keep track of file data
        ArrayList<Integer> ips_track = new ArrayList<>();
        ArrayList<String> ips_string = new ArrayList<>();
        
        try
        {
            //takes constructor line input in as scanner
            Scanner scan = new Scanner(new File(args[0]));
            
            //while reading file...
            while(scan.hasNextLine())
            {
                //set line to the String from arraylist line
                String line = scan.nextLine();
                
                //seperate line in its different segments to isolate ip
                String[] spl = line.split(" ");
                
                //if length is more than 10...
                if(spl.length == 10)
                {
                    //find ip and temporarily set x as ip
                    int x = ips_string.indexOf(spl[9]);
                    //check if fails
                    if(x > -1)
                    {
                        Integer temp = ips_track.get(x);
                        ips_track.set(x,new Integer(temp.intValue() + 1));
                    }
                    else
                    {
                        //if fails add to track arraylist
                        ips_string.add(spl[9]);
                        ips_track.add(new Integer(1));
                    }
                }
            }
            
            //create new file to display output
            File myObj = new File(args[1]);
            
            if (myObj.createNewFile())
            {
                System.out.println("File created: " + myObj.getName());
            }
            else 
            {
                System.out.println("File already exists");
            }
        }
        //catch
        catch(Exception e)
        {
            e.printStackTrace();
            System.exit(0);
        }
        
        //add data from ips_string by using track to see how many times 
        //the ip failed
        FileWriter myWriter=null;
        try
        {
            myWriter = new FileWriter(args[1]);
            for(int i = 0;i<ips_track.size();i++)
            {
                int temp = ips_track.get(i);
                if(temp >= 3)
                {
                    myWriter.write(ips_string.get(i)+"\n");
                    //print final output
                    System.out.println(ips_string.get(i));
                }
            }
            //closes file
            myWriter.close();
        
        }
        //catch
        catch (IOException e)
        {
            System.out.println("An error occurred");
            e.printStackTrace();
        }
    }
}

