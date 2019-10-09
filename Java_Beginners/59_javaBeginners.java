// apples.java file

class Apples{
	public static void main(String[] args){

		DogList DLO = new DogList();
		Dog d = new Dog();
		DLO.add(d);
	}
}

//Dog.java file

public class Dog extends Animal{

}

//Fish.java file

public class Fish extends Animal{

}

//Animal.java file

public class Animal{

}

//DogList.java file

public class DogList{
	private Dog[] thelist = new Dog[5];
	private int i=0;

	public void add(Dog d){
		if(i<thelist.length){
			thelist[i]=d;
			System.out.println("Dog added at index "+i);
			i++;
		}
	}
}
