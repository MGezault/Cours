import java.io.FileReader;
import java.util.ArrayList;
import com.google.gson.Gson;

public class Box{
    ArrayList<Thing> contents;
    boolean ouverte= false;
    int volume = -1;

    public Box (boolean etat,int volume){
        this.volume = volume;
        this.ouverte=etat;
        this.contents= new ArrayList<>();
    }

    public void add(Thing truc) {
        this.contents.add(truc);
    }
    public boolean contient(Thing truc){
        if (this.contents.contains(truc)) {return true;}
        return false;
    }
    public boolean supprimer(Thing truc){
        if (this.contient(truc)){this.contents.remove(truc); return true;}
        return false;
    }

    public boolean isOpen(){
        return this.ouverte;
    }
    public void close(){
        this.ouverte = false;
    }
    public void open(){
        this.ouverte = true;
    }
    public int capacity(){
        return this.volume;
    }

    public String actionLook(){
        if (this.ouverte) {return "la boite contient:" + this.contents;}
        return "La boite est fermée";
    }

    public boolean hasRoomFor(int t){
        if (t<= this.volume) {return true;}
        if (this.volume == -1) {return true;}
        return false;
    }

    public void actionAdd(Thing t){
        if (this.ouverte){
            if (this.hasRoomFor(t.getPoids())){
                this.contents.add(t);
                if (this.volume != -1) {this.volume -= t.getPoids();}
             }
        }
    }

    public boolean hasName(String nom){
        for (Thing chose : this.contents){
            if (chose.getName().equals(nom)) {return  true;}
        }
        return false;
    }


    public Thing find(String nom){
        if (this.ouverte){
            for (Thing chose : this.contents){
                if (chose.getName().equals(nom)) {return chose;}
            }
        }
        return null;
    }

    public Box fromJSON(String json){
        FileReader fr= new FileReader("BoxFromJson.json");
        Gson gson = new Gson();
        Box maboite = gson.fromJson(fr, Box.class);
        return maboite;
    }

}