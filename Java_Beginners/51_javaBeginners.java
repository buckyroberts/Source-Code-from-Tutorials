//tuna.java file
import java.awt.FlowLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class tuna extends JFrame{
	
	private JLabel item1;
	
	public tuna(){
		super("The title bar");
		setLayout(new FlowLayout());
		
		item1 = new JLabel("this is sentence");
		item1.setToolTipText("This is gona show up on hover");
		add(item1);
	}
	
}
//apples.java
import javax.swing.JFrame;

class apples {
	public static void main(String[] args){
		
		tuna bucky = new tuna();
		bucky.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		bucky.setSize(275,180);
		bucky.setVisible(true);
	}
}
