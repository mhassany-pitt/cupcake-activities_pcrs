// Write your code here
public class LinkedListExample {
    // the LinkedListExample class' properties
	private Node head;
	private int size;
	
	private class Node {
        // the Node class' properties
		Node next;
		String data;
	}
	// Constructor! This initializes a new empty LinkedListExample:
	public LinkedListExample()
	{
		head = null;
		size = 0;
	}
	
    // This method adds a Node to the LinkedListExample by creating a new Node out of a String
    // The String becomes the new Node's data, and then the Node gets attached to the end of the LinkedListExample
	public boolean add(String val){
		Node curr = head;
        if (curr == null) {
			head = new Node(val);
        }
		else {
			while (curr.next != null){
				curr = curr.next;
			}
			curr.next = new Node(val);
		}
		size++;
		return true;
	}
    
    // This method returns the entire Node at a given "index" (loc)
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
    
	// This method returns a Node's data from a given "index" (loc)
	public String get(int loc){
		Node curr = getNodeAt(loc);
		if (curr != null)
			return curr.data;
		else
			return null;
	}
    
	// This method just returns the LinkedListExample's size
	public int size()
	{
		return size;
	}
    
    // TODO: Complete this function to stitch together two LinkedListExample objects
    // Parameters: two LinkedListExample objects
    // Returns: one new LinkedListExample object made out of the two parameter objects
	public LinkedListExample mergeLists(LinkedListExample list2){
        // mergedList is what this method eventually returns
        // It's initialized here for you, and right now it's blank
        LinkedListExample mergedList = new LinkedListExample();
// Write your code here
        return mergedList;
	}   
}