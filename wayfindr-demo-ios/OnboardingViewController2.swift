//
//  OnboardingViewController.swift
//  Wayfindr Demo
//
//  Created by Alex Caskey on 15/11/2018.
//  Copyright © 2018 Wayfindr.org Limited. All rights reserved.
//

import Foundation


public class OnboardingViewController2 : UIViewController {
    
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
    
    }
    
    @IBAction func clickNext(_ sender: Any){
        self.view.window!.rootViewController?.dismiss(animated: false, completion: nil)
    }
}
