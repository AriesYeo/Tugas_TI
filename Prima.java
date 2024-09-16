import java.util.Scanner;

public class Prima {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = input.nextInt();
        
        if (isPrime(n)) {
            System.out.println(n + " adalah bilangan prima.");
        } else {
            System.out.println(n + " tidak adalah bilangan prima.");
        }
        input.close();
    }

    //cek apakah bilangan tersebut ada prima atau bukan
    public static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

/**
 * Pseudocode:
    Start
        Input number n
        If n is less than 2, then it's not prime.
        Loop from i = 2 to sqrt(n):
        If n % i == 0, then n is not prime.
        If no divisors were found, then n is prime.
    End
 */