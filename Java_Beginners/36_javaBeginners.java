public class apples {
    public static void main(String[] args) {
        tuna tunaObject = new tuna();
        System.out.println(tunaObject.toMilitary());
        tunaObject.setTime(13, 27, 6);
        System.out.println(tunaObject.toMilitary());
    }

}

public class tuna {
    private int hour;
    private int minute;
    private int second;
    
    public void setTime(int h, int m, int s){
        hour = ((h>=0 && h<24) ? h : 0);
        minute = ((m>=0 && m<60) ? m : 0);
        hour = ((s>=0 && s<60) ? s : 0);
    }
    
    public  String toMilitary(){
        return String.format("%02d:%02d:%02d", hour, minute, second);
    }
}