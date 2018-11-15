package com.example.hein.hackgui;


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class Question4Activity extends AppCompatActivity {

    Button theButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_question3b);
        theButton = findViewById(R.id.btn_next3);
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
        startActivity(new Intent(this, Question4bActivity.class));
    }
}