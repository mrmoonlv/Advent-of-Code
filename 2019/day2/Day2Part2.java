import java.io.File;
import java.util.Scanner;

class Day2Part2 {
    public static int cursor = 0;
    public static int result_need = 19690720;
    public static String map[];

    public static void initMap() throws Exception
    {
        Scanner scanner = new Scanner( new File("data.txt") );
        String text = scanner.useDelimiter("\\A").next();
        scanner.close();
        map =text.split(",");
    }

    public static void main(String[] args) throws Exception
    {
        for(int noun = 0; noun < 100; noun++) {
            for(int verb = 0; verb < 100; verb++) {
                initMap();
                cursor = 0;
                map[1] = Integer.toString(noun);
                map[2] = Integer.toString(verb);
                while(true){
                    int method = Integer.parseInt(map[cursor]);

                    int a_key = Integer.parseInt(map[cursor+1]);
                    int a = Integer.parseInt(map[a_key]);
                    int b_key = Integer.parseInt(map[cursor+2]);
                    int b = Integer.parseInt(map[b_key]);
                    int position_key = Integer.parseInt(map[cursor+3]);

                    if(method == 1){
                        map[position_key] = Integer.toString(a + b);
                    } else if (method == 2) {
                        map[position_key] = Integer.toString(a * b);
                    } else { //99
                        break;
                    }

                    cursor = cursor + 4;

                    if(Integer.parseInt(map[0]) == result_need ){
                        System.out.println("FOUND: " +  noun  + verb);
                        System.exit(0);
                    }
                }
            }
        }
    }
}