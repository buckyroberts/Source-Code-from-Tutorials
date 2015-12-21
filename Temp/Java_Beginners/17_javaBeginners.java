import java.util.Scanner;
class apples{
    public static void main(String args[]){
        tuna tunaObject = new tuna();
        tuna tunaobject2 = new tuna();
        tunaObject.saying();
        tunaObject2.saying();
    }
}
public class tuna {
    private String girlName;

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