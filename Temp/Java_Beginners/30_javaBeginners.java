import java.util.Random;

class apples{
    public static void main(String[] args){
        Random rand = new Random();
        int freq[]=new int[7];
        
        for(int roll=1;roll<1000;roll++){
            ++freq[1+rand.nextInt(6)];
        }

        System.out.println("Face\tFrequency");

        for(int face=0;face<freq/length;face++){
            System.out.println(face+"\t"+freq[face]);
        }
    }
}