/*Main.java*/
import javax.swing.*;

public class Main {
    public static void main (String[] args) {

        TheWindow w = new TheWindow();
        w.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        w.setSize(230, 280);
        w.setVisible(true);

    }
}





/*TheWindow.java*/
import java.awt.*;
import javax.swing.*;
import javax.swing.event.*;

public class TheWindow extends JFrame{

    private JSlider slider;
    private DrawOval myPanel;

    public TheWindow(){
        super("The title");
        myPanel = new DrawOval();
        myPanel.setBackground(Color.ORANGE);

        slider = new JSlider(SwingConstants.HORIZONTAL, 0, 200, 10);
        slider.setMajorTickSpacing(10);
        slider.setPaintTicks(true);

        slider.addChangeListener(
                new ChangeListener(){
                    public void stateChanged(ChangeEvent e){
                        myPanel.setD(slider.getValue());
                    }
                }
        );

        add(slider, BorderLayout.SOUTH);
        add(myPanel, BorderLayout.CENTER);

    }
}





/*DrawOval.java*/
import java.awt.*;
import javax.swing.*;

public class DrawOval extends JPanel{

    private int d = 10;

    public void paintComponent(Graphics g){
        super.paintComponent(g);
        g.fillOval(10, 10, d, d);
    }

    public void setD(int newD){
        d = (newD >= 0 ? newD : 10);
        repaint();
    }

    public Dimension getPreferredSize(){
        return new Dimension(200,200);
    }

    public Dimension getMinimumSize(){
        return getPreferredSize();
    }
}