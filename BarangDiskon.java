import java.util.Scanner;

public class BarangDiskon{
   public static void main(String args[]){    
    Scanner input = new Scanner (System.in);
 
    System.out.print("Masukkan Kode Barang: ");
    String kodebarang = input.nextLine();

    System.out.print("Masukkan Harga Barang: ");
    double hargabarang = input.nextDouble();

    System.out.print("Masukkan Jumlah Barang: ");
    int Jumlah = input.nextInt();

    double bayar = hargabarang * Jumlah;
    
    double discount = 0;

    if (bayar > 150000) {
        discount = bayar * 0.05; // 5% discount jika pembayaran > 150,000
    }

    double totalBayar = bayar - discount;

    System.out.println("Barang Dengan Kode: " + kodebarang);
    System.out.println("Total bayar setelah diskon: " +  totalBayar);

    input.close();
    
}
} 