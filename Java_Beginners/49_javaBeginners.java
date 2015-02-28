public class apples {
    public static void main(String[] args){
        tuna tunaObject = new tuna();
        potpie potObject = new potpie();
        
        tunaObject.eat();
        potObject.eat();
        
    }
}

public class tuna extends food {
    public void eat(){
        System.out.println("I am the new method of tuna");        
    }
}

public class potpie extends food{

}

public class food {
    public void eat(){
        System.out.println("I am the eat methods");        
    }
}