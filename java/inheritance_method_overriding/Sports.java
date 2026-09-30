public class Sports{

    String getName(){
        return "Generic Sports";
    }
  
    void getNumMembers(){
        System.out.println( "The team has n players in " + getName() );
    }
}

class Basketball extends Sports{
    @Override
    String getName(){
        return "Basketball Class";
    }
    // TODO: add your method here
    
    
}