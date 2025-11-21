import java.util.PriorityQueue;
import java.util.List;
import java.util.ArrayList;

public class KBestCounter<T extends Comparable<? super T>> {
    PriorityQueue<T> heap;
    int k;


    public KBestCounter(int k) {
        this.k=k;
        heap = new PriorityQueue();//todo
    }

    public void count(T x) {
        heap.add(x);//todo
        
        if(heap.size()>k){
            heap.poll();
        }
            
            
    }

    public List<T> kbest() {
        //todo
        PriorityQueue<T> heap2 = new PriorityQueue(heap);
        List<T> result = new ArrayList<>();
        
        while (!heap2.isEmpty()){
            result.add(heap2.poll());
        }
        
        return result; // replace this
    }
    
}
