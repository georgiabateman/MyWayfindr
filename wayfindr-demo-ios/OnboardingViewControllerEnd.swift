//
//  OnboardingViewController.swift
//  Wayfindr Demo
//
//  Created by Alex Caskey on 15/11/2018.
//  Copyright © 2018 Wayfindr.org Limited. All rights reserved.
//

import Foundation


public class OnboardingViewControllerEnd : UIViewController {
    
    @IBOutlet weak var textview: UITextView!
    @IBOutlet weak var button: UIButton!
    
    override public func viewDidLoad() {
        super.viewDidLoad()
        let currentBackground = UIColor.black
        let currentText = UIColor.yellow
        
        self.view.backgroundColor = currentBackground
        
        textview.backgroundColor = currentBackground
        textview.textColor = currentText
        
        button.backgroundColor = currentBackground
        button.tintColor = currentText
        button.layer.cornerRadius = 5
        button.layer.borderWidth = 2
        button.layer.borderColor = currentText.cgColor
    }
    
    @IBAction func clickFinish(_ sender: Any) {
        self.view.window!.rootViewController?.dismiss(animated: true, completion: nil)
    }
}
