import java.io.File;
import java.text.DecimalFormat;
import java.util.Scanner;

class Day1Part1 {

	private static double total;

	public static void main(String[] args) throws Exception
	{

		File file = new File("data.txt");
		Scanner sc = new Scanner(file);

		while (sc.hasNextLine()) {

			double line_int = Integer.valueOf(sc.nextLine());
			line_int =  Math.floor(line_int / 3 ) -2;
			System.out.println(line_int);
			total = total + line_int;
		}

		System.out.println("INPUT:");
		DecimalFormat format = new DecimalFormat("0.#");
		System.out.println(format.format(total));
	}
}
