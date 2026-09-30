static int indOfMin( int[] arr, int count, int startingAt){
    int minIndex = startingAt;
    int min = arr[startingAt];
    for(int i=startingAt+1;i<count;i++){
        if(arr[i]<min){
            minIndex = i;
        }
    }
    return minIndex;
}
    
static void sortArray(int arr[], int count){
	//TODO: write your code here
    //Make sure you use the method indOfMin to solve this problem (for more detailed guidance, check the description of the problem)
    
    
    
}
      