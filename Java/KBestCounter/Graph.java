import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.LinkedList;
import java.util.Deque;
import java.util.Collection;
import java.lang.Math;
import java.util.PriorityQueue;
import java.util.ArrayList;


public class Graph<V> {
   
    // Keep an index from node labels to nodes in the map
    protected Map<V, Vertex<V>> vertices;

    /**
     * Construct an empty Graph.
     */
    public Graph() {
       vertices = new HashMap<V, Vertex<V>>();
    }

    /**
     * Retrieve a collection of vertices.
     */  
    public Collection<Vertex<V>> getVertices() {
        return vertices.values();
    }

    public void addVertex(V u) {
        addVertex(new Vertex<>(u));
    }
   
    public void addVertex(Vertex<V> v) {
        if (vertices.containsKey(v.name))
            throw new IllegalArgumentException("Cannot create new vertex with existing name.");
        vertices.put(v.name, v);
    }

    /**
     * Add a new edge from u to v.
     * Create new nodes if these nodes don't exist yet.
     * @param u unique name of the first vertex.
     * @param w unique name of the second vertex.
     * @param cost cost of this edge.
     */
    public void addEdge(V u, V w, Double cost) {
        if (!vertices.containsKey(u))
            addVertex(u);
        if (!vertices.containsKey(w))
            addVertex(w);

        vertices.get(u).addEdge(
            new Edge<>(vertices.get(u), vertices.get(w), cost));

    }

    public void addEdge(V u, V w) {
        addEdge(u,w,1.0);
    }

    public void printAdjacencyList() {
        for (V u : vertices.keySet()) {
            StringBuilder sb = new StringBuilder();
            sb.append(u.toString());
            sb.append(" -> [ ");
            for (Edge e : vertices.get(u).getEdges()){
                sb.append(e.target.name);
                sb.append(" ");
            }
            sb.append("]");
            System.out.println(sb.toString());
        }
    }    
 
   /**
    * Add a bidirectional edge between u and v. Create new nodes if these nodes don't exist
    * yet. This method permits adding multiple edges between the same nodes.
    *
    * @param u  
    *          the name of the source vertex.
    * @param v
    *          the name of the target vertex.
    * @param cost
    *          the cost of this edge
    */
    public void addUndirectedEdge(V u, V v, Double cost) {
        addEdge(u,v, cost);
        addEdge(v,u, cost);
    }

    /****************************
     * Your code follows here.  *
     ****************************/
   
//Part 1
    public void computeAllEuclideanDistances(){
        for(Vertex<V> s: getVertices()){
            for(Edge city: s.getEdges()){
                Vertex<V> t = city.target;
                //coordinates 
                int x1 = s.posX;
                int y1 = s.posY;
                int x2 = t.posX;
                int y2 = t.posY;
                //distance calculator 
                double d = Math.sqrt(Math.pow(x2-x1,2)+ Math.pow(y2-y1,2));
                city.distance = d;
            }
        }
    }


//Part 2 
    public void doDijkstra(V s){
    
        for(Vertex<V> v: getVertices()){
            v.cost= Double.POSITIVE_INFINITY;
            v.visited = false;
            v.backpointer= null;
  
        }
    
  
        //TA
        PriorityQueue<Vertex<V>> queue = new PriorityQueue<>((Vertex<V> v1, Vertex<V> v2) -> Double.compare( v1.cost,v2.cost));
    
  
        Vertex<V> startCity = vertices.get(s);
        startCity.cost = 0.0;
        startCity.visited= true;
        queue.add(startCity);
        Vertex<V> finalDest;
        Vertex<V> next;
        while(!(queue.isEmpty())){
            next = queue.poll();
            next.visited=true;
       
            for(Edge<V> city: next.getEdges()){
                finalDest=city.target;
                if((finalDest.visited==false)&&(next.cost+city.distance)<(finalDest.cost)){
                    finalDest.cost=next.cost+city.distance;
                    finalDest.backpointer=next;
                    queue.add(finalDest);
           
                }  
            }
        }
    }
    
    //Part 3
    public List<Edge<V>> getDijkstraPath(V s, V t){
    
        doDijkstra(s);
    
   
        LinkedList<Edge<V>> finalpath = new LinkedList<Edge<V>>();
    
 
        Vertex<V> current = vertices.get(t);
    
 
        while(current.backpointer != null){
            Edge<V> city = new Edge(current.backpointer, current);
            finalpath.add(city);
            current = current.backpointer;
 
        }
    
 
        //return final path
   
        return finalpath;

    }

}


