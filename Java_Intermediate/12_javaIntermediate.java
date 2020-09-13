import java.util.*;

public class Main {

    public static void main (String[] args) {

        //convert stuff array to a list
        String[] stuff = {"apples", "beef", "corn", "ham"};
        List<String> list1 = Arrays.asList(stuff);

        ArrayList<String> list2 = new ArrayList<String>();
        list2.add("youtube");
        list2.add("google");
        list2.add("digg");

        for (String x : list2){
            System.out.printf("%s ", x);
        }

        Collections.addAll(list2, stuff);

        System.out.println();
        for (String x : list2){
            System.out.printf("%s ", x);
        }
    }
}