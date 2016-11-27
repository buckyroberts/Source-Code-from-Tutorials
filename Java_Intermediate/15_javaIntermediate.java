import java.util.*;

public class Main {

    public static void main (String[] args) {

        PriorityQueue<String> q = new PriorityQueue<String>();

        q.offer("first");
        q.offer("second");
        q.offer("third");

        System.out.printf("%s ", q);
        System.out.println();

        System.out.printf("%s ", q.peek());
        System.out.println();

        q.poll();
        System.out.printf("%s ", q);
    }
}