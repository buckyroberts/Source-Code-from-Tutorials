public class apples {
    public static void main(String[] args){
        for(tuna people: tuna.values())            
            System.out.printf("%s\t%s\t%s\n", people, people.getDesc(), people.getYear());
    }
}

public enum tuna {
    bucky("nice", "22"),
    kelsey("cutie", "10"),
    julia("bigmistake", "12");
    
    private final String desc;
    private final String year;
    
    tuna(String description, String birthday){
        desc = description;
        year = birthday;
    }
    
    public String getDesc(){
        return desc;
    }
    
    public String getYear(){
        return year;
    }
}