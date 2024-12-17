package graphs;

import java.util.ArrayList;

public class BinarySearch {
	public int search(ArrayList<Integer> array, int target) {
		int left= 0;
		int right= array.get(array.size()-1);
		
		while (left <= right){
			int mid=(int) Math.round((double) (left + right) / 2);
			
			if (array.get(mid) == target) return mid;
			else if (array.get(mid) > target) right= mid-1;
			else left= mid+1;
		}
		
		return -1;
	}
	
	public static void main(String[] args) {
		int k = 10;
		ArrayList<Integer> l= new ArrayList<Integer>(k);
		
		for (int i=0; i<2*k; i+=2) {
			l.add(i);
		}
		
		BinarySearch bin= new BinarySearch();
		int index= bin.search(l, 16);
		
		if (index != -1) {
			System.out.print("Element found at position ");
			System.out.println(index); 
		}else {
			System.out.println("Element was not found!");
		}
		
	}

}
