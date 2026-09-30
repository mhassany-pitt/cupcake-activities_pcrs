public class LinkedList {
	private Node head;
	private int size;
	
	private class Node {
		Node next;
		String data;
		// Node constructor:
		public Node(String dataValue) {
			next = null;
			data = dataValue;
		}
		// Node constructor with next:
		public Node(String dataValue, Node nextValue){
			next = nextValue;
			data = dataValue;
		}
	}
	// Initialize a new empty LinkedList:
	public LinkedList()
	{
		head = null;
		size = 0;
	}
    private Node getNodeAt(int loc)
	{
		if (loc >= 0 && loc < size)
		{
			Node curr = head;
			for (int i = 0; i < loc; i++)
				curr = curr.next;
			return curr;
		}
		return null;
	}
    
	// Return item at stated index:
	public String get(int loc){
		Node curr = getNodeAt(loc);
		if (curr != null)
			return curr.data;
		else
			return null;
	}
	// Return logical size of list:
	public int size()
	{
		return size;
	}
    
    // TO DO: Complete this function to traverse through the LinkedList and return its contents
    // as a single String with no characters separating the elements.
    // Hint: Use the traversal techniques shown for other methods above to travel
    // element-by-element through your LinkedList, as well as other methods within 
    // this class to access elements.
	public String traverseList(){
        String retStr = "";
// Write your code here
        return retStr;
	}   
}