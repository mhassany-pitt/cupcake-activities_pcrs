// Write your code here
public class Truck { 
    private String model;
    private int year;
    private String color;
 	private double maxCapacity;
    //If currentLoad is 0.0 the truck is empty, if equals to maxCapacity the truck is full
    private double currentLoad;
    
    public Truck(){
        this.model = "default model";
        this.year = 2000;
        this.color= "default color";
        this.maxCapacity = 1800.0;
        this.currentLoad = 0.0;     
    }
    
    public Truck(String truckModel, int truckYear, String truckColor, double truckMaxCapacity, double truckCurrentLoad){
    	model = truckModel;
        year = truckYear;
        color = truckColor;
        maxCapacity = truckMaxCapacity;
        currentLoad = truckCurrentLoad;   
    }
    
    // TODO: add get/set methods for model, year, color, maxCapacity and currentLoad
    // There has to be 10 methods in total here (setModel, getModel, setYear, getYear, setColor, getColor, setMaxCapacity, getMaxCapacity, setCurrentLoad, getCurrentLoad).
    
    
    
    
    
    
    
    
    //TODO: complete the load and unload methods by using the getCurrentLoad, 
    // setCurrentLoad and getMaxCapacity methods.
    public void load(double weightLoaded){
    //Important: validate that the updated currentLoad cannot be greater than maxCapacity
    //if this happens, only load the part of the loaded weight that will make the truck full
    
        
        
    }
    
    public void unload(double weightUnloaded){
    //Important: validate that it cannot be unloaded more weight than the currentLoad
    //if this happens, just unload the feasible part of the unloaded weight that will make the truck empty
        
        
    
    }
    
}