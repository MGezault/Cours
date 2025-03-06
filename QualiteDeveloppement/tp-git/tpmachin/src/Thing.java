public class Thing{

    String name;
    int poids;
    public Thing(String name){
        this.name = name;
        this.poids = -1;
    }
    public Thing(String name,int poids){
        this.name = name;
        this.poids = poids;
    }
    public int getPoids(){
        return this.poids;
    }

    public String getName(){
        return this.name;
    }
    public void setCapacity(int volume){
        this.poids = volume;
    }

    public void setName(String nom){
        this.name = nom;
    }


    @Override
    public boolean equals(Object objet){
        if (objet == null) {return false;}
        if (this ==objet){return true;}
        if (!(objet instanceof Thing)){return false;}

        Thing tmp = (Thing) objet;
        return (tmp.poids== this.poids) && tmp.name.equals(this.name);
    }

    @Override
    public String toString(){
        return "Nom : " + this.name + ", Poids : " + this.poids;
    }
}
    