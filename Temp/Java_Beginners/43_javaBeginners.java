public class apples {
    public static void main (String[] args){
        potpie potObject = new potpie(4,5,6);
        tuna tunaObject = new tuna("Bucky", potObject);
        
        System.out.println(tunaObject);
    }
}

public class tuna {
    private String name;
    private potpie birthday;
    
    public tuna(String theName, potpie theDate){
        name = theName;
        birthday = theDate;
    }
    
    public String toString(){
        return String.format("My name is %s, my birthday is %s", name, birthday);
    }
}

public class potpie {
    public int month;
    public int day;
    public int year;
    
    public potpie(int m, int d, int y){
        month = m;
        day = d;
        year = y;
        
        System.out.printf("The constructor for this is %s\n", this);
    }
    
    public String toString(){
        return String.format("%d/%d/%d", month, day, year);
    }
}