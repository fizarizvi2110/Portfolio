import java.util.Scanner;
public class GuessRandom {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        System.out.println("I'm thinking of a number between 1 to 10, inclusive. What do you think it is?");
        int guess = in.nextInt();
        double x = Math.random();
        int rand = (int)(x * 10) + 1;
        guessingGame(rand, guess);
    }
    public static void guessingGame(int rand, int guess){
        if (guess == rand){
            System.out.println("Correct! You guessed the number " + rand);
        }
        else {
            if (guess != rand){
                int diff = Math.abs(rand - guess);
                System.out.println("The number was " + rand + ". You were off by " + diff);
            }
        }
        
    }

}
