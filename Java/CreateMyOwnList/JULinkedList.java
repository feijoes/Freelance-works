
import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;

public class JULinkedList <T> implements List {

    private class Node{
        Object data;
        Node next;
        Node(Object data){
            this.data = data;
            next=null;
        }

    }
    Node head;






    @Override
    public int size() {
      if (head == null){
          return 0;
      }
      Node temp = head;
      int count = 0;
      while (temp!=null){
          count++;
          temp = temp.next;
      }
      return count;
    }
    @Override
    public boolean isEmpty() {
        if(head==null){
            return true;
        }

        return false;
    }

    @Override
    public boolean contains(Object o) {
        if(head==null){
            return false;
        }
        Node current = head;
        while(current != null && !current.data.equals(o)){

            current = current.next;
        }
        if(current.data.equals(o)){
            return true;
        }
        return false;
    }

    @Override
    public Iterator <T>iterator() {
        if(head.next != null){
            return (Iterator<T>) head.next;
        }

        return null;
    }

    @Override
    public Object[] toArray() {
        return new Object[0];
    }

    @Override
    public boolean add(Object o) {

        Node toinsert = new Node(o);
        if(head ==null){
            head = toinsert;
            return true;
        }
        Node temp = head;
        while (temp.next!=null){
            temp=temp.next;
        }
        temp.next= toinsert;
        return true;
    }

    @Override
    public boolean remove(Object o) {
        Node current = head;
        Node temp = null;
        if(o == head.data){
            head = current.next;
            return true;
        }

        while(current != null && !current.data.equals(o)){
            temp = current;
            current = current.next;
        }

        if(current == null){
            return true;
        }

        temp.next = current.next;
        return false;
    }




    @Override
    public boolean addAll(Collection c) {
        return false;
    }

    @Override
    public boolean addAll(int index, Collection c) {
        return false;
    }

    @Override
    public void clear() {
        head = null;

    }

    @Override
    public Object get(int index) {
        if (head == null){
            return null;
        }


        Node temp = head;


        if(index < 0 || index >=size()){
            return null;
        }else if(index == 0){


            return head.data;
        }else {

            Node previous = head;
            int count = 1;
            while(count < index - 1){
                previous = previous.next;
                count++;
            }

            Node current = previous.next;

            return current.data;
        }
    }

    @Override
    public Object set(int index, Object element) {
        Node node = head;

        if(index == 1){
            node.next = head;
            head = node;
        } else {
             Node previous = head;
            int count = 1; // position - 1

            while(count < index - 1){
                previous = previous.next;
                count++;
            }

            Node current = previous.next;
            previous.next = node;
            node.next = current;
        }

        return element;
    }

    @Override
    public void add(int index, Object element) {

    }

    @Override
    public Object remove(int index) {
        if (head == null){
            return null;
        }


        Node temp = head;


        if(index < 0 || index >=size()){
            return null;
        }else if(index == 0){

            head = head.next;
            temp.next = null;
            return temp;
        }else {

            Node previous = head;
            int count = 1;
            while(count < index - 1){
                previous = previous.next;
                count++;
            }

            Node current = previous.next;
            previous.next = current.next;
            return current.data;
        }
    }

    @Override
    public int indexOf(Object o) {

        return 0;
    }

    @Override
    public int lastIndexOf(Object o) {
        return 0;
    }

    @Override
    public ListIterator listIterator() {
        return null;
    }

    @Override
    public ListIterator listIterator(int index) {
        return null;
    }

    @Override
    public List subList(int fromIndex, int toIndex) {
        return null;
    }

    @Override
    public boolean retainAll(Collection c) {
        return false;
    }

    @Override
    public boolean removeAll(Collection c) {
        return false;
    }

    @Override
    public boolean containsAll(Collection c) {
        return false;
    }

    @Override
    public Object[] toArray(Object[] a) {
        return new Object[0];
    }
}
