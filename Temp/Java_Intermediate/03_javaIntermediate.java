public class Main {

    //main
    public static void main(String[] args) {
        System.out.println(fact(5));
    }

    //fact
    public static long fact(long n) {
        if (n <= 1) {
            return 1;
        }

        return n * fact(n-1);
    }
}