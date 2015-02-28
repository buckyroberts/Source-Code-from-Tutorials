import java.util.Scanner;

class apples{
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        int total = 0;
        int grade;
        int average;
        int counter;

        while (counter < 10){
            grade = input.nextInt();
            total = total + grade;
            counter++;
        }
        average = total/10
        System.out.println("Your average is "+ average);
    }
}