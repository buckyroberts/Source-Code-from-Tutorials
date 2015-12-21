package aybars.arslan.sqqlitesample;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;


public class MainActivity extends ActionBarActivity {

    EditText etInput;
    TextView txtText;
    Button btnAdd, btnDelete;
    MyDBHandler dbHandler;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btnAdd = (Button)findViewById(R.id.btnAdd);
        btnDelete = (Button)findViewById(R.id.btnDelete);
        etInput = (EditText)findViewById(R.id.etInput);
        txtText = (TextView)findViewById(R.id.txtText);

        dbHandler = new MyDBHandler(this, null, null, 1);
        try {
            printDatabase();
        }catch (Exception e){
            Log.i("exxxx", e.toString());
        }

    }

    public void printDatabase() {
        String dbString = dbHandler.databaseToString();
        txtText.setText(dbString);
        etInput.setText("");
    }

    //Add a product to the database
    public void addButtonClicked(View view){
        Log.i("exxxx", "CLİCKED ADD BUTTON");
        String product = etInput.getText().toString();
        Products p = new Products(product);
        dbHandler.addProduct(p);
        printDatabase();
    }

    //Delete a product to the database
    public void deleteButtonClicked(View view){
        Log.i("exxxx", "CLİCKED DELETE BUTTON");
        String inputText = etInput.getText().toString();
        dbHandler.deleteProduct(inputText);
        printDatabase();
    }
}
