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
        return source.stream()
            .map(s -> mapper.apply(s))
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
        return IntStream.iterate(1, power -> power * base);
    }

    public static String say() {
        return "";
    }

    static class Sayer {
        String text;
        Sayer(String text) {
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

    public static Optional<String> firstLongStringUppercased(int length, List<String> strings) {
        return strings.stream()
            .filter(s -> s.length() > length)
            .findFirst()
            .map(s -> s.toUpperCase());
    }

    private static class Player {
        String name;
        int games;
        int points;
        String team;
        Player(String[] description) {
            this.name = description[0];
            this.games = Integer.parseInt(description[1]);
            this.points = Integer.parseInt(description[2]);
            this.team = description[3];
        }
        double ppg() {
            return (double) points / games;
        }
        @Override public String toString() {
            return String.format("%s|%.2f|%s",
                    name, ppg(), team);
        }
    }

    public static List<String> topTenScorers(Map<String, List<String>> statistics) {
        return statistics.keySet().stream()
            .flatMap(team -> 
                statistics.get(team).stream()
                    .map(stats -> (stats + "," + team)
                        .split(",")))
            .map(Player::new)
            .filter(player -> player.games >= 15)
            .sorted((p1, p2) ->
                Double.compare(p2.ppg(), p1.ppg()))
            .limit(10)
            .map(player -> player.toString())
            .collect(Collectors.toList());
    }

}