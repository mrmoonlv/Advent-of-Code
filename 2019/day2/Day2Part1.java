import java.io.File;
import java.util.Scanner;
class Day2Part1 {
	public static int cursor = 0;
	public static String map[];
	public static int exitProgram(){
		System.out.println("FOUND: " + Integer.parseInt(map[0]));
		System.exit(0);
		return 0;
	}
	public static int updateStep(){
		int method = Integer.parseInt(map[cursor]);
		if(method == 99) {
			exitProgram();
		}
		int a_key = Integer.parseInt(map[cursor+1]);
		int a = Integer.parseInt(map[a_key]);
		int b_key = Integer.parseInt(map[cursor+2]);
		int b = Integer.parseInt(map[b_key]);
		int position_key = Integer.parseInt(map[cursor+3]);
		int value = (method == 1) ? a + b : a * b; //method 1 + //method 2 *
		//UPDATE
		map[position_key] = Integer.toString(value);
		//GO NEXT CURSOR
		if(cursor != 99) {
			cursor = cursor + 4;
			updateStep();
		} else {
			exitProgram();
		}
		return 1;
	}
	public static void main(String[] args) throws Exception
	{
		Scanner scanner = new Scanner( new File("data.txt") );
		String text = scanner.useDelimiter("\\A").next();
		scanner.close();
		map = text.split(",");
		map[1] = "12";
		map[2] = "2";
		updateStep();
	}
}