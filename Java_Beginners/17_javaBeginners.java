import java.util.Scanner;
class apples{
    public static void main(String args[]){
        tuna tunaObject = new tuna("String 1");
        tuna tunaObject2 = new tuna("String 2");
        tunaObject.saying();
        System.out.println();
        tunaObject2.saying();
    }
}
public class tuna {
    private String girlName;
    //default constructor 
    public tuna(){}
    //parametrised constructor
    public tuna(String name){
        girlName=name;
    }

    public String getName(){
        return girlName;
    }
    public void saying(){
        System.out.printf("Your first gf was %s", getName());
    }
}
