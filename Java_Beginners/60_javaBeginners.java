// apples.java file

class apples{
	public static void main(String[] args){

		AnimalList ALO = new AnimalList();
		Dog d = new Dog();
		Fish f = new Fish();
		ALO.add(d);
		ALO.add(f);
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

//AnimalList.java file

public class AnimalList{

	private Animal[] thelist = new Animal[5];
	private int i = 0;

	public void add(Animal a){
		if(i<thelist.length){
			thelist[i]=a;
			System.out.println("Animal added at index "+a);
			i++;
		}
	}
}
