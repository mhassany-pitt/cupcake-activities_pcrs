public class Truck { 
    private String model;
    private int year;
    private String color;
 	private double maxCapacity;
    //If currentLoad is 0.0 the truck is empty, if equals to maxCapacity the truck is full
    private double currentLoad;
    
    // TODO: complete the class constructors here
    public Truck(){
        
        
        
        
    }
    
    public Truck(String model, int year, String color, double maxCapacity, double currentLoad){
    
        
        
        
    }
    
    // TODO: add get/set methods for model, year, color, maxCapacity and currentLoad
    // There has to be 10 methods in total here (setModel, getModel, setYear, getYear, setColor, getColor, setMaxCapacity, getMaxCapacity, setCurrentLoad, getCurrentLoad).
    
    
    
    
    
    
    
    
    //TODO: complete the load and unload methods by using the getCurrentLoad, 
    // setCurrentLoad and getMaxCapacity methods.
    public void load(double weight){
    //Important: validate that the updated currentLoad cannot be greater than maxCapacity
    //if this happens, only load the part of the loaded weight that will make the truck full
    
        
        
    }
    
    public void unload(double weight){
    //Important: validate that it cannot be unloaded more weight than the currentLoad
    //if this happens, just unload the feasible part of the unloaded weight that will make the truck empty
        
        
    
    }
    
}