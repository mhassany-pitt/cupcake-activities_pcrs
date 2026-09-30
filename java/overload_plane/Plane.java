public class Plane {
    private String airline;
    private String model;
    private double mileage;
    private float flightHours;
    
    final int AVG_SPEED = 550;//average speed of the plane in mph
    final int MAX_SPEED = 750;//max speed of the plane in mph
    
    public Plane(){
        mileage = 0.0;
        flightHours = 0.0f;
        airline = "LATAM";
        model = "Boeing 787";
    }
    
    public Plane(String airline, String model, double mileage, float flightHours){
		this.airline = airline;
        this.model = model;
        this.mileage = mileage;
        this.flightHours = flightHours;
    }
    
    public void setAirline(String airline){
    	this.airline = airline;
    }
    
    public String getAirline(){
    	return airline;
    }
    
    public void setModel(String model){
    	this.model = model;
    }
    
    public String getModel(){
    	return model;
    }
    
    // TODO: add the missing getters/setters for mileage and flightHours
    
    
    
    
    // TODO: add the 4 overloaded fly methods
    

        
        
    
    
    
}