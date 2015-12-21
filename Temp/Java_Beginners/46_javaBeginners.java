public class apples {
    public static void main(String[] args){
        tuna member1 = new tuna("Megan", "Fox");
        tuna member2 = new tuna("Natalie", "Portman");
        tuna member3 = new tuna("Taylor", "Swift");
    }

}

public class tuna {
    private String first;
    private String last;
    private static int members = 0; 
    
    public tuna(String fn, String ln){
        first = fn;
        last = ln;
        members++;
        System.out.printf("Constructor for %s %s, members in the club : %d\n", first, last, members);
    }
}