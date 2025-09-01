public class Example1{

    private String flavor;
    //encapsulation
    public void setFlavor(String newFlavor){
        flavor=newFlavor;
    }

    public String getFlavor(){
        return flavor;
    }

    public void openBag(){
        System.out.println("Bag is opened!");
    }

}