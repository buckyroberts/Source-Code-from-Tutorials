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
 
 //apples.java file
 
 class apples {
	 public static void main(String[] args)
	 {
		 food bucky[] = new food[2];
		 bucky[0]=new potpie();
		 bucky[1]=new tuna();
		 
		 for(int x=0;x<2;++x){
			 bucky[x].eat();
		 }
	 }
 }
 