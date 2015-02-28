public class Main {

    public static void main(String[] args) {

        String s = "buckyrobertsbuckyroberts";

        System.out.println(s.indexOf("rob", 10));

        String a = "BACON ";
        String b = "monster";
        String c = "     flying        ";

        System.out.println(a.concat(b));
        
        System.out.println(a.replace('B', 'F'));
        
        System.out.println(b.toUpperCase());
        
        System.out.println(a.toLowerCase());
        
        System.out.println(c.trim());

    }

}