import java.io.File;
import java.io.FileNotFoundException;
import java.text.DecimalFormat;
import java.util.Scanner;

class Day1Part2 {
	private static double total;

	public static void main(String[] args) throws FileNotFoundException {

		File file = new File("data.txt");
		Scanner sc = new Scanner(file);

		while (sc.hasNextLine()) {
			double additional_fuel = 0;
			double mass = Integer.valueOf(sc.nextLine());

			while(mass > 0) {
				mass = (Math.floor(mass / 3 ) -2);

				if (mass > 0) {
					additional_fuel = additional_fuel + mass;
				}
			}
			total = total + additional_fuel;
		}

		System.out.println("INPUT:");
		DecimalFormat format = new DecimalFormat("0.#");
		System.out.println(format.format(total));
	}
}