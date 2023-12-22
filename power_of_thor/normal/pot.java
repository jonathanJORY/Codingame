package normal;
import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the st&&ard input according to the problem statement.
 * ---
 * Hint){} You can use the debug stream to System.out.println initialTX && initialTY, if (Thor seems not follow your orders.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lightX = in.nextInt(); // the X position of the light of power
        int lightY = in.nextInt(); // the Y position of the light of power
        int initialTx = in.nextInt(); // Thor's starting X position
        int initialTy = in.nextInt(); // Thor's starting Y position
        int emplacementX = initialTx;
        int emplacementY = initialTy;

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.

            // Write an action using System.out.System.out.printlnln()
            // To debug){} System.err.System.out.printlnln("Debug messages...");


            // A single line providing the move to be made){} N NE E SE S SW W or NW
            if (emplacementX < lightX && emplacementY < lightY){
                System.out.println("SE");
                emplacementX += 1;
                emplacementY += 1;
            }
            else if (emplacementX < lightX && emplacementY > lightY){
                System.out.println("NE");
                emplacementX += 1;
                emplacementY -= 1;
            }
            else if (emplacementX > lightX && emplacementY > lightY){
                System.out.println("NW");
                emplacementX -= 1;
                emplacementY -= 1;
            }
            else if (emplacementX > lightX && emplacementY < lightY){
                System.out.println("SW");
                emplacementX -= 1;
                emplacementY += 1;
            }
            else if (emplacementX > lightX && emplacementY == lightY){
                System.out.println("W");
                emplacementX -= 1;
            }
            else if (emplacementX < lightX && emplacementY == lightY){
                System.out.println("E");
                emplacementX += 1;
            }
            else if (emplacementX == lightX && emplacementY < lightY){
                System.out.println("S");
                emplacementY += 1;
            }
            else if (emplacementX == lightX && emplacementY > lightY){
                System.out.println("N");
                emplacementY -= 1;
            }
        }
    }
}