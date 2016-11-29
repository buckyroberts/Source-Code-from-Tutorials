import java.net.*;
import java.util.*;
import java.awt.*;
import java.applet.*;
import javax.swing.*;
import javax.swing.event.*;

public class BuckySites extends JApplet {

    private HashMap<String, URL> websiteInfo;
    private ArrayList<String> titles;
    private JList mainList;

    //init
    public void init(){
        websiteInfo = new HashMap<String, URL> ();
        titles = new ArrayList<String>();

        grabHTMLInfo();
        add(new JLabel("What website do you want to visit?"), BorderLayout.NORTH);
        mainList = new JList(titles.toArray());

        mainList.addListSelectionListener(
                new ListSelectionListener(){
                    public void valueChanged(ListSelectionEvent event){
                        Object object = mainList.getSelectedValue();
                        URL newDocument = websiteInfo.get(object);
                        AppletContext browser = getAppletContext();
                        browser.showDocument(newDocument);
                    }
                }
        );
        add(new JScrollPane(mainList), BorderLayout.CENTER);
    }

    //get website info
    private void grabHTMLInfo(){
        String title;
        String address;
        URL url;
        int counter = 0;
        title = getParameter("title" + counter);

        while(title != null){
            address = getParameter("address" + counter);
            try{
                url = new URL(address);
                websiteInfo.put(title, url);
                titles.add(title);
            }catch(MalformedURLException urlException){
                urlException.printStackTrace();
            }
            ++counter;
            title = getParameter("title" + counter);
        }
    }
}