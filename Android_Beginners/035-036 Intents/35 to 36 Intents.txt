[source code] Android Development Tutorial - 35 and 36 - Intents

***** Apples.java (MainActivity)

package your.package.intentexample;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;

public class Apples extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_apples);
    }

    public void baconClick(View view){
        Intent I = new Intent(this, Bacon.class);
        // get user input
        final EditText userInput = (EditText) findViewById(R.id.ptvUserInput);
        String userMessage = userInput.getText().toString();
        // pass user input in the intent
        I.putExtra("applesMessage", userMessage);

        startActivity(I);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}


***** activity_apples.xml

<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
    android:layout_height="match_parent" android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    android:paddingBottom="@dimen/activity_vertical_margin" tools:context=".MainActivity"
    android:background="#009900">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textAppearance="?android:attr/textAppearanceLarge"
        android:text="@string/tvApplesText"
        android:id="@+id/tvApples"
        android:layout_alignParentTop="true"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="84dp" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/btnBacon"
        android:id="@+id/btnBacon"
        android:layout_centerVertical="true"
        android:layout_centerHorizontal="true"
        android:onClick="baconClick"/>

    <EditText
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/ptvUserInput"
        android:layout_below="@+id/tvApples"
        android:layout_marginTop="42dp"
        android:width="250dp"
        android:layout_centerHorizontal="true"
        android:hint="Enter a message for the Bacon Activity" />

</RelativeLayout>

***** Strings.xml

<resources>
    <string name="app_name">Intent Example</string>

    <string name="action_settings">Settings</string>
    <string name="tvApplesText">Apples</string>
    <string name="btnBacon">Go To Bacon</string>
    <string name="title_activity_bacon">Bacon</string>
    <string name="tvBacon">Bacon</string>
    <string name="btnApplesText">Go To Apples</string>
</resources>

***** Bacon.java (Second Activity)
package your.package.intentexample;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

public class Bacon extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_bacon);

        Bundle appleData = getIntent().getExtras();
        if (appleData== null){
            return;
        }
        String applesMessage = appleData.getString("applesMessage");
        TextView tvBacon = (TextView) findViewById(R.id.tvBacon);
        tvBacon.setText(applesMessage);
    }
    public void applesClick(View view){
        Intent I = new Intent(this, Apples.class);
        startActivity(I);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_bacon, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}


***** activity_Bacon.xml

<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
    android:layout_height="match_parent" android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    android:paddingBottom="@dimen/activity_vertical_margin"
    tools:context="your.package.intentexample.Bacon"
    android:background="#72231f">


    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:textAppearance="?android:attr/textAppearanceLarge"
        android:text="@string/tvBacon"
        android:id="@+id/tvBacon"
        android:layout_marginTop="82dp"
        android:singleLine="true"
        android:layout_alignParentTop="true"
        android:layout_centerHorizontal="true" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/btnApplesText"
        android:id="@+id/btnApples"
        android:layout_centerVertical="true"
        android:layout_centerHorizontal="true"
        android:onClick="applesClick" />
</RelativeLayout>