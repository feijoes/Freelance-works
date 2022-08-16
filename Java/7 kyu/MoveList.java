class Node{
  public int data;
  public Node next = null;
  
  public static int getNth(Node n, int index) throws Exception{
    if(index == 0){
      return n.data;
    }
       
    if(index < 0){
      Node c = n;
      int len = 1;
      while(c.next != null){
        len++;
        c = c.next;
      }
            
      
        
      for(int i = 1;i<=(len-index);i++){
      n=n.next;
    }
      
    return n.data;
    }else{
    for(int i = 1;i<=index;i++){
      n=n.next;
    }
    return n.data;
  }
