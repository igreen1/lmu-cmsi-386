import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;

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
        var codePoints = s.replaceAll("\\s","").codePoints().toArray();
        String result = "";
        for(int i = 0; i < codePoints.length; i++){
            result += Character.toChars(codePoints[i]).toString().repeat(i);
        }
        return result;
    }




}