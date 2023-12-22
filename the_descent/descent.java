package the_descent;
import java.util.*;

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> hauteurs = new ArrayList<>(); // Initialisez la liste

        // game loop
        while (true) {
            hauteurs.clear(); // Videz la liste à chaque itération
            for (int i = 0; i < 8; i++) {
                int mountainH = in.nextInt(); // represents the height of one mountain.
                hauteurs.add(mountainH);
            }

            // Trouver la montagne la plus haute
            int max_index = 0;
            for (int i = 0; i < hauteurs.size(); i++) {
                if (hauteurs.get(i) > hauteurs.get(max_index)) {
                    max_index = i;
                }
            }

            // Imprimer l'index de la montagne la plus haute
            System.out.println(max_index);
        }
    }
}
