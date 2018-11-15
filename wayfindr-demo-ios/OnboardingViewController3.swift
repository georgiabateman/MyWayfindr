//
//  OnboardingViewController.swift
//  Wayfindr Demo
//
//  Created by Alex Caskey on 15/11/2018.
//  Copyright © 2018 Wayfindr.org Limited. All rights reserved.
//

import Foundation


public class OnboardingViewController3 : UIViewController {
    
    @IBOutlet weak var textview: UITextView!
    @IBOutlet weak var button1: UIButton!
    @IBOutlet weak var button2: UIButton!
    
    override public func viewDidLoad() {
        super.viewDidLoad()
        let currentBackground = UIColor.black
        let currentText = UIColor.yellow
        
        self.view.backgroundColor = currentBackground
        
        textview.backgroundColor = currentBackground
        textview.textColor = currentText
        
        button1.backgroundColor = currentBackground
        button1.tintColor = currentText
        button1.layer.cornerRadius = 5
        button1.layer.borderWidth = 2
        button1.layer.borderColor = currentText.cgColor
        
        button2.backgroundColor = currentBackground
        button2.tintColor = currentText
        button2.layer.cornerRadius = 5
        button2.layer.borderWidth = 2
        button2.layer.borderColor = currentText.cgColor
    }
    
    @IBAction func clickNext(_ sender: Any){
        self.view.window!.rootViewController?.dismiss(animated: false, completion: nil)
    }
}
