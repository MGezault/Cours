public class Personnage {
    private String nom;
    private int tailleDeBarbe;
    private int tailleDesOreilles;

    public Personnage(String nom, int barbe, int oreille){
    this.nom = nom;
    this.tailleDeBarbe =  barbe;
    this.tailleDesOreilles = oreille;
    }


    public String getNom(){
    return this.nom;
    }

    public int getBarbe(){
        return this.tailleDeBarbe;
    }

    public int getTailleDesOreilles(){
        return this.tailleDesOreilles;
    }
}