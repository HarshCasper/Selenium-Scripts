import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {

		int limit = 1000000; 
		int size = 0, max = 1, j = 0;
		for (int i = 2; i < limit; i++) {
			size = getChainSize(i);
			if (size > max) {
				max = size;
				j = i;
			}
		}
		System.out.println("Starting number, under one million, produces the longest chain is : " + j);
	}

	private static int getChainSize(int n) {

		long num = n;
		List<Long> list = new ArrayList<>();
		int size = 0;
		while (num != 1) {
			list.add(num);
			if (num % 2 == 0) {
				num = num / 2;
			} else {
				num = 3 * num + 1;
			}
		}
		size = list.size();
		return size;
	}

}
