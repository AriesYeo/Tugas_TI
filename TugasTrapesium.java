import java.util.Scanner;

public class TugasTrapesium{
   public static void main(String args[]){    
    Scanner input = new Scanner (System.in);
 
    System.out.print("Masukkan panjang sisi alas a: ");
    double a = input.nextDouble();
    System.out.print("Masukkan panjang sisi atas b: ");
    double b = input.nextDouble();
    System.out.print("Masukkan panjang garis miring c: ");
    double c = input.nextDouble();
    System.out.print("Masukkan panjang garis miring d: ");
    double d = input.nextDouble();
    System.out.print("Masukkan tinggi trapesium e: ");
    double e = input.nextDouble();
    
    double luas = ((a + b) * e) / 2;

    double keliling = a + b + c + d;

    System.out.println("Luas Trapesium: " + luas);
    System.out.println("Keliling Trapesium: " + keliling);

    input.close();
    
}
} 