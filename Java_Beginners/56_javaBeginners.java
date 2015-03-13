//food.java file

public class food{
	void eat(){
				System.out.println(" this food is great");
}

//tuna.java file

public class tuna extends food{
	void eat(){
				System.out.println(" this tuna is great");
}

//potpie.java file
	
	public class potpie extends food{
			void eat(){
				System.out.println(" this potpie is great");
			}
	}
 
//fatty.java file

public class fatty{
	public void digest(food x){
		x.eat();
	}
}
//apples.java file
public static void main(String[] args)
{
	fatty bucky = new fatty();
	food fo = new food();
	food po = new potpie();
	
	bucky.digest(fo);
	bucky.digest(po);
}