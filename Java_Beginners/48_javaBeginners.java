public class apples {
    public static void main(String[] args){
        tuna tunaObject = new tuna(10);
        
        for(int i=0; i<5;i++){
            tunaObject.add();
            System.out.printf("%s", tunaObject);
        }
    }
}

public class tuna {
    private int sum;
    private final int NUMBER;
    
    public tuna(int x){
        NUMBER = x;
    }
    public void add(){
        sum+=NUMBER;
    }
    public String toString(){
        return String.format("sum = %d\n", sum);
    }

}