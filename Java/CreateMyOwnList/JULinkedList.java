
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
        return null;
    }

    @Override
    public Object set(int index, Object element) {
        return null;
    }

    @Override
    public void add(int index, Object element) {

    }

    @Override
    public Object remove(int index) {
        return null;
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
