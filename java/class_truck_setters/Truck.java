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
    // TODO: add set methods for model, year, color, maxCapacity and currentLoad
    // There has to be 5 methods in total here (setModel, setYear, setColor, setMaxCapacity, setCurrentLoad).
    
    
    
    
}