package insertionsSort;

public class InsertionSort {
	
	public void insertionSort(int []change){
		int temp;
		for(int i = 0;i < change.length;i++){
			int j = i-1;
			while(j >= 0){
				if(change[j] > change[j + 1]){
					temp = change[j];
					change[j] = change[j + 1];
					change[j + 1] = temp;
				}
				j--;
			}
		
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] change = {5, 2, 10, 6, 2};
		InsertionSort chain = new InsertionSort();
		chain.insertionSort(change);
		for(int i = 0; i < change.length;i++){
			System.out.print(change[i]);
		}
	}

}
