import java.util.ArrayList;
import java.util.List;

public class MergeSortArrayList {

    public static List<Integer> sort(List<Integer> list) {
        if (list.size() <= 1) {
            return list;
        }

        int mid = list.size() / 2;
        // Skapa sub-listor (subList skapar en vy, så vi kopierar till nya ArrayLists)
        List<Integer> left = sort(new ArrayList<>(list.subList(0, mid)));
        List<Integer> right = sort(new ArrayList<>(list.subList(mid, list.size())));

        return merge(left, right);
    }

    private static List<Integer> merge(List<Integer> left, List<Integer> right) {
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0;

        while (i < left.size() && j < right.size()) {
            if (left.get(i) <= right.get(j)) {
                result.add(left.get(i));
                i++;
            } else {
                result.add(right.get(j));
                j++;
            }
        }

        // Lägg till resterande element
        while (i < left.size()) result.add(left.get(i++));
        while (j < right.size()) result.add(right.get(j++));

        return result;
    }
}