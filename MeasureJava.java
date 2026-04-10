import Algoritmer.*;
import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

public class MeasureJava {

    private static ArrayList<Integer> loadList(String filename) throws Exception {
        File file = new File("Data/" + filename);
        ArrayList<Integer> data = new ArrayList<>();
        try (Scanner sc = new Scanner(file)) {
            while (sc.hasNextInt()) {
                data.add(sc.nextInt());
            }
        }
        return data;
    }

    private static ArrayList<ArrayList<Integer>> loadMatrix(String filename) throws Exception {
        File file = new File("Data/" + filename);
        ArrayList<ArrayList<Integer>> matrix = new ArrayList<>();
        try (Scanner sc = new Scanner(file)) {
            while (sc.hasNextLine()) {
                String line = sc.nextLine().trim();
                if (line.isEmpty()) continue;
                String[] values = line.split(",");
                ArrayList<Integer> row = new ArrayList<>();
                for (String v : values) {
                    row.add(Integer.parseInt(v.trim()));
                }
                matrix.add(row);
            }
        }
        return matrix;
    }

    public static void main(String[] args) {
        if (args.length < 3) return;

        String algo = args[0];
        String fileA = args[1];
        int runs = Integer.parseInt(args[2]);

        try {
            if (algo.equals("matrix")) {
                String fileB = args[3];
                ArrayList<ArrayList<Integer>> A = loadMatrix(fileA);
                ArrayList<ArrayList<Integer>> B = loadMatrix(fileB);
                
                for (int i = 0; i < runs; i++) {
                    long start = System.nanoTime();
                    MatrixMath.multiply(A, B);
                    long end = System.nanoTime();
                    System.out.println(end - start);
                }
            } else {
                ArrayList<Integer> data = loadList(fileA);
                for (int i = 0; i < runs; i++) {
                    ArrayList<Integer> copy = new ArrayList<>(data);
                    long start = System.nanoTime();
                    if (algo.equals("quick")) {
                        QuickSort.quickSort(copy, 0, copy.size() - 1);
                    } else if (algo.equals("merge")) {
                        MergeSortArrayList.sort(copy);
                    }
                    long end = System.nanoTime();
                    System.out.println(end - start);
                }
            }
        } catch (Exception e) {
            System.err.println("Java Error: " + e.getMessage());
        }
    }
}