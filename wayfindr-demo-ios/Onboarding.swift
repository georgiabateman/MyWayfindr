public class Onboarding {
    static let sharedInstance :Onboarding = {
        let instance = Onboarding()
        // setup code
        return instance
    }()
    
    var pos = 0;
    
    public init() {
        print("StartOnboarding")
        //Onboarding.sharedInstance.pos = 0;
    }
    
    public func updatePosition(to: Int32) {
        
        print("update position from %s to %s", Onboarding.sharedInstance.pos, to)
    }
    
    public func incrementPosition(){
        Onboarding.sharedInstance.pos = Onboarding.sharedInstance.pos+1;
    }
}
