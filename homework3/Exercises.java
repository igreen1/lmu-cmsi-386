import java.util.*;
import java.util.stream.*;
import java.util.function.*;
import java.util.Optional;
import java.util.Map;
import java.math.*;

public class Exercises {

    public static List<Integer> change(int amount) {
        if (amount  < 0) {
            throw new IllegalArgumentException("Amount cannot be negative");
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
            result += String.copyValueOf(Character.toChars(codePoints[i])).repeat(i+1);
        }
        return result;
    }

    public static <T,U> Set<U> mapThenUnique(List<T> source, Function<T,U> mapper) {
        return source.stream() //Toal's example started with return Set.of(), not sure if it matters
            .map( (s) -> mapper.apply(s))
            .collect(Collectors.toSet());
    }

    public static void powers(int base, int limit, Consumer<Integer> consumer) {
        int power = 1;
        while (power <= limit) {
            consumer.accept(power);
            power *= base;
        }
    }

    public static IntStream powers(int base) {
        return IntStream.iterate(1, i -> i * base);
    }

    public static String say() {
        return "";
    }

    static class Sayer {
        String text;
        Sayer(String text) {    //constructor
            this.text = text;
        } 
        String ok() {
            return this.text;
        }
        Sayer and(String s) {
            return new Sayer(this.text + " " + s);
        }
    }

    public static Sayer say(String text) {
        return new Sayer(text);
    }

    public static <T> T twice(Function<T, T> f, T x) {
        return f.apply(f.apply(x));
    }

    public static Optional<String> firstLongStringUppercased(int length, List<String> Strings) {
        Optional<String> upperCase = Strings.stream()
            .filter( (s) -> s.length() > length)
            .findFirst()
            .map( (s) -> s.toUpperCase());
        return upperCase;
    }

    public static List<String> topTenScorers(Map<String, List<String>> statistics) {
        return statistics.entrySet().stream()
        .flatMap(team -> team.getValue().stream().map(player -> player += "," + team.getKey()))
        .filter(player -> Integer.parseInt(player.split(",")[1]) >= 15)
        .map(player -> {var playerStats = player.split(",");
            var ppg = Double.parseDouble(playerStats[2]) / Double.parseDouble(playerStats[1]);
            return playerStats[0] + "|" + String.format("%.2f", ppg) + "|" + playerStats[3];} )
        .sorted(new Comparator<String>(){
            @Override
            public int compare(String player1, String player2){
                return Double.compare(Double.parseDouble(player2.split("\\|")[1]), Double.parseDouble(player1.split("\\|")[1]));
            }
        }).limit(10).collect(Collectors.toList());
    } 

}