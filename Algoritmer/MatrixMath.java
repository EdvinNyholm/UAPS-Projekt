package Algoritmer;
import java.util.ArrayList;

public class MatrixMath {
    public static ArrayList<ArrayList<Integer>> multiply(ArrayList<ArrayList<Integer>> A, 
                                                         ArrayList<ArrayList<Integer>> B) {
        int rowsA = A.size();
        int colsA = A.get(0).size();
        int colsB = B.get(0).size();

        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < rowsA; i++) {
            ArrayList<Integer> newRow = new ArrayList<>();
            for (int j = 0; j < colsB; j++) {
                int sum = 0;
                for (int k = 0; k < colsA; k++) {
                    // Hämtar elementen och multiplicerar
                    sum += A.get(i).get(k) * B.get(k).get(j);
                }
                newRow.add(sum);
            }
            result.add(newRow);
        }
        return result;
    }
}