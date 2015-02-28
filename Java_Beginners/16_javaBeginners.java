import java.util.Scanner;
class apples{
    public static void main(String args[]){
    
        Scanner input = new Scanner(System.in);
        tuna tunaObject = new tuna();
        System.out.println("Enter name of first gf here: ");
        String temp = input.nextLine();
        tunaObject.setName(temp);
        tunaObject.saying();
    }
}


public class tuna {
    private String girlName;
    public void setName(String name){
        girlName=name;
    }
    public String getName(){
        return girlName;
    }
    public void saying(){
        System.out.printf("Your first gf was %s", getName());
    }
}