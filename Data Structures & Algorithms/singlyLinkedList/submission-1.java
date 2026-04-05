class LinkedList {
    class Node {
        int value;
        Node next;
        
        //constructor
        public Node( int value) {
            this.value = value;
            this.next = null;
        }
    }
    Node head;
    public LinkedList() {
        this.head = null;
    }

    public int get(int index) {
        int count = 0;
        Node tempCopy = this.head;
        while (tempCopy != null) {
            if(count == index){
                return tempCopy.value;
            }
            count++;
            tempCopy = tempCopy.next;
        }
        return -1;
    }

    public void insertHead(int val) {

        //make a new node
        Node newHead = new Node(val);
        //make newHead point to old head
        newHead.next = this.head;
        //label newHead as head
        this.head = newHead;

    }

    public void insertTail(int val) {
        
        Node newTail = new Node(val);
        if (this.head == null) {
            this.head = newTail;
            return;
        }
        Node curr = this.head;

        while (curr.next != null) {
            curr = curr.next;
        }
        //move newTail @ curr.next
        curr.next = newTail;
    }

    public boolean remove(int index) {
        if (this.head == null){
            return false;
        }
        int count = 1;
        Node curr = this.head;
        if(index == 0) {
            this.head = this.head.next;
            return true;
        }
        while (curr.next != null) {

            if (count == index) {
                curr.next = curr.next.next;
                return true;
            }
            count++;
            curr = curr.next;
        }
        return false;
        
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<Integer>();
        Node curr = this.head;
        while (curr != null){

                values.add(curr.value);
                curr = curr.next;
        }
        return values;
    }
}
