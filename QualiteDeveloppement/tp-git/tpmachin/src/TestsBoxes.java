import org.junit.*;
    public class TestsBoxes {
    @Test
    public void testBoxCreate() {
        Box b = new Box(false,15);
    }
        /** on veut pouvoir mettre des trucs dedans */
    @Test
    public void testBoxAdd(){
        Box b = new Box(true,5);
        b.add(new Thing("truc1",2));
        b.add(new Thing("truc2",1));
    }
    @Test(expected = ArithmeticException.class)
    public void divisionWithException() {
        int i = 1/0;
}
}