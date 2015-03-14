package aybars.arslan.fragments;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.app.Activity;
import android.widget.Button;
import android.widget.EditText;

public class TopSectionFragment extends Fragment {

    private static EditText etTopTextInput;
    private static EditText etBottomTextInput;

    TopSectionListener activityCommander;

    public interface TopSectionListener{
        public void createClick(String top, String bottom);
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        try{
            activityCommander = (TopSectionListener) activity;
        }catch (ClassCastException e){
            throw new ClassCastException(activity.toString());
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.top_section_fragment, container, false);

        etTopTextInput = (EditText)view. findViewById(R.id.etTopTextInput);
        etBottomTextInput = (EditText)view.findViewById(R.id.etBottomTextInput);

        final Button button = (Button)view.findViewById(R.id.btn);

        button.setOnClickListener(
                new View.OnClickListener(){

                    @Override
                    public void onClick(View v) {
                        buttonClicked(v);
                    }
                }
        );

        return view;
    }

    //Calls this when button clicked
    public void buttonClicked(View view){
        activityCommander.createClick(etTopTextInput.getText().toString(), etBottomTextInput.getText().toString());
    }
}
