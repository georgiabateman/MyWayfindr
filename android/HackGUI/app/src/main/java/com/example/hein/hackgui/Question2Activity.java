package com.example.hein.hackgui;


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class Question2Activity extends AppCompatActivity {

    ImageView theButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_question1);
        theButton = findViewById(R.id.phone_icon1);
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
        startActivity(new Intent(this, Question3Activity.class));
    }
}

