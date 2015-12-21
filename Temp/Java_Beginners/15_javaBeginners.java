import java.util.Scanner;
class apples{
    public static void main(String args[]){
    
        Scanner input = new Scanner(System.in);
        tuna tunaObject = new tuna();
        
        System.out.println("Enter your name here: ");
        String name = input.nextLine();
        
        tunaObject.simpleMessage(name);

    }
}


public class tuna {
    public void simpleMessage(String name){
        System.out.println("Hello " + name);
    }
}