package com.example.hein.hackgui;


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class Question1Activity extends AppCompatActivity {

    Button theButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_question0);
        theButton = findViewById(R.id.btn_next2);
        if (theButton != null) {
            theButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    NAVIGATE();
                }
            });
        }
    }

    private void NAVIGATE() {
        startActivity(new Intent(this, Question2Activity.class));
    }
}


