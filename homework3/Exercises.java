import java.util.*;
import java.util.stream.*;
import java.util.function.*;
import java.util.Optional;

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
        Optional<String> upperCaseString = Strings.stream()
            .filter( (s) -> s.length() > length)
            .findFirst()
            .map( (s) -> s.toUpperCase());
        return upperCaseString;
    }

    public static List<String> topTenScorers(Map<String, List<String>> statistics) {
        // Stream<String> stream = statistics.stream();
            // JS CODE TO TRANSLATE:
            // .flatMap( ([team, players]) -> players.map( player -> [...player,team]))
            // .filter( ([, games, ,]) -> games >= 15)
            // .map( ([name, games, points, team]) -> ({ name, ppg: points / games, tean}))
            // .sort( (p1,p2) -> p2.ppg - p1.ppg)
            // .slice(0,10);
        // return List.of(stream);
        return List.of();
    } 

}