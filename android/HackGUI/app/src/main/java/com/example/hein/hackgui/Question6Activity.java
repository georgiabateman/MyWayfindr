package com.example.hein.hackgui;


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class Question6Activity extends AppCompatActivity {

    Button theButton;
    Button theButton2;
    private View.OnClickListener theListener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            NAVIGATE();
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_question5_2);
        theButton = findViewById(R.id.btn_yes6);
        theButton2 = findViewById(R.id.btn_no6);
        if (theButton != null) {
            theButton.setOnClickListener(theListener);
        }
        if (theButton2 != null) {
            theButton2.setOnClickListener(theListener);
        }
    }

    private void NAVIGATE() {
        startActivity(new Intent(this, Question7Activity.class));
    }
}

