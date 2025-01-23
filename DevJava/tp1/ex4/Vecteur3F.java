public class Vecteur3F {
    private double x;
    private double y;
    private double z;
    public Vecteur3F(double x, double y, double z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
    public Vecteur3F(){
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    public Vecteur3F(Vecteur3F Vecteur){
        this.x = Vecteur.x;
        this.y = Vecteur.y;
        this.z = Vecteur.z;
    } 

    public double getX(){
        return this.x;
    }

    public double getY(){
        return this.y;
    }

    public double getZ(){
        return this.z;
    }

    public void modifier(double k, int xyz){
        if (xyz==1)
        this.x = k;
        else{
        if (xyz == 2)
        this.y = k;
        
        else 
        this.z = k;
        }
    }

    public double getNorme(){
        return Math.sqrt((this.x * this.x + this.y *this.y + this.z* this.z));
    }

    @Override

    public String toString(){
    return "Vecteur3F <" + this.x + " " + this.y + " " + this.z + "> De Norme : " + this.getNorme(); 
    }
}
