public static int countAllChildren(Node node) {
    // TODO
    
}
class Node{
   public int id;
   public Node parent;
   public ArrayList<Node> children;//How many direct children a node has
    
   public Node(int id){
      this.id = id;
      parent = null;
      children = new ArrayList<Node>();
   }
    
   public void addChildren(Node child){
      children.add(child);
   }        
}   