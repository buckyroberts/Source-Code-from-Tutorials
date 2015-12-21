import java.util.*;

public class Main {

    public static void main(String[] args) {

        String[] things = {"eggs", "lasers", "hats", "pie" };
        List<String> list1 = new ArrayList<String>();

        //add array items to list
        for (String x: things) {
            list1.add(x);
        }

        String[] morethings = {"lasers", "hats" };
        List<String> list2 = new ArrayList<String>();

        //add array items to list
        for (String y: morethings) {
            list2.add(y);
        }

        for (int i = 0; i < list1.size(); i++) {
            System.out.printf("%s ", list1.get(i));
        }
    }
}