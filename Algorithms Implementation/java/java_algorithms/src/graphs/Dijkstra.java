package graphs;
import java.util.ArrayList;
import java.util.PriorityQueue;

public class Dijkstra {
    
    private PriorityQueue<int[]> queue;
    private ArrayList<Integer> weights;
    private ArrayList<Boolean> visited;
    private ArrayList<Integer> parents;
    
    public Dijkstra() {
        this.queue = new PriorityQueue<>((o1, o2) -> Integer.compare(o1[0], o2[0]));
        this.weights = new ArrayList<>();
        this.visited = new ArrayList<>();
        this.parents = new ArrayList<>();
    }
    
    public ArrayList<Integer> exec(int[][] graph, int origin, int objective) {
        for (int i = 0; i < graph.length; i++) {
            weights.add(Integer.MAX_VALUE);
            parents.add(-1);
            visited.add(false);
        }
        
        queue.add(new int[] {0, origin});
        weights.set(origin, 0);
        
        while (!queue.isEmpty() && !visited.get(objective)) {
            int[] node = queue.poll();
            
            if (visited.get(node[1])) continue;
            visited.set(node[1], true);
            
            relax(graph, node[1]);
        }
        return buildPath(this.parents, origin, objective);
    }
    
    private void relax(int[][] graph, int index) {
        for (int i = 0; i < graph[index].length; i++) {
            if (graph[index][i] > 0 && !visited.get(i)) {
                int localWeight = weights.get(index) + graph[index][i];
                
                if (localWeight < weights.get(i)) {
                    weights.set(i, localWeight);
                    parents.set(i, index);
                    
                    queue.add(new int[] {localWeight, i});
                }
            }
        }
    }
    
    private ArrayList<Integer> buildPath(ArrayList<Integer> parents, int origin, int destiny){
    	ArrayList<Integer> path= new ArrayList<Integer>();
    	int currentPar= destiny;
    	
    	while (currentPar!= origin){
    		if (currentPar==-1) return null;
    		path.add(currentPar);
    		currentPar= this.parents.get(currentPar);	
    	}
    	
    	path.add(origin);
    	
    	ArrayList<Integer> reversedPath= new ArrayList<Integer>(path.size());
    	for (int i= path.size()-1; i>=0; i--) {
    		reversedPath.add(path.get(i));
    	}
    	
    	return reversedPath;
    }
    
    public int getPathWeight(int destiny) {
    	return this.weights.get(destiny);
    }
    
    public static void main(String[] args) {
        int[][] graph = {
            {0, 1, -1, -1},
            {1, 0, -1, 10},
            {2, -1, 0, 2},
            {-1, -1, 2, 0}
        };
        
        int origin= 0;
        int destiny= 3;
        
        Dijkstra d = new Dijkstra();
        ArrayList<Integer> path= d.exec(graph, origin, destiny);
        
        if (path== null) {
        	System.out.println("There is no path between origin and destiny!");
        	System.out.println("Check your graph.");
        	
        }else {
        	System.out.println("Path encountered:");
            System.out.println(path);
            
            System.out.print("Weight: ");
            System.out.println(d.getPathWeight(destiny));
        }
    }
}
