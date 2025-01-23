public class ExecutablePersonnage {
    public static void main(String [] args) {
    Personnage nain = new Personnage("Gimli", 65, 15);
    System.out.println(nain.getNom());
    System.out.println(nain.getTailleDesOreilles());
    System.out.println(nain.getBarbe());
    
    // Tests
    Personnage hagrid = new Personnage("Hagrid", 84, 21);
    Personnage Nolhan = new Personnage("Nolhan", 1, 5);
    assert Nolhan.getBarbe() == 1;
    assert hagrid.getTailleDesOreilles() == 21;
    assert hagrid.getNom() == "Hagrid";
    assert Nolhan.getTailleDesOreilles() == 5;
    }
}