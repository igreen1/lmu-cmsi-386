import java.util.*;

public class Exercises {

    public static List<Integer> change(int amount) {
        if (amount  < 0) {
            throw new IllegalArgumentException();
        }
        var denominations = List.of(25, 10, 5, 1);
        var coinCounts = new ArrayList<Integer>();
        for (var denomination: denominations) {
            coinCounts.add(amount / denomination);
            amount %= denomination;
        }
        return List.copyOf(coinCounts);
    }

    public static String stretched(String s) {
        return "";
    }
}