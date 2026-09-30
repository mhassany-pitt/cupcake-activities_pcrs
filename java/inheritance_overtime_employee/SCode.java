// Write your code here
class Employee {
	private int hours;
	private double hourlyRate;
    
	public int getHours() {
		return hours;
	}
	
	public double hourlyRate() {
		return hourlyRate;
	}
    
    public double getSalary(){
        // TODO: Write your code here (implement getSalary())
        
       
    }
    
	public Employee(int hours, double hourlyRate){
		this.hours = hours;
		this.hourlyRate = hourlyRate;
	}
}

class OvertimeEmployee extends Employee {
	public double overtimeFactor;
    
    public OvertimeEmployee(int hours, double hourlyRate, double overtimeFactor) {
		super(hours, hourlyRate);
		this.overtimeFactor = overtimeFactor;
	}
    
	// TODO: Write your code here (override getSalary())

    
    
    
    
    
    
    
}