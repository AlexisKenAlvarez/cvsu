/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inventorymanager;
import java.util.ArrayList;
import java.util.List;
import java.util.*;

/**
 *
 * @author ASUS
 */
public class InventoryManager{
    
    // INITIALIZING ARRAYLISTS FOR THE INVENTORY
    private final List<String> brands = new ArrayList<>();
    private final ArrayList<String> singlesProd = new ArrayList<>();
    private final ArrayList<String> boxedProd = new ArrayList<String>();
    private final ArrayList<String> totalProd = new ArrayList<String>();
    
    // Convert brand ArrayList to array
    String[] brandList = new String[brands.size()];

    void add(SingleProduct p){ 
       singlesProd.add(p.getBrand());
       String myBrand = p.getBrand();
       brands.add(myBrand);
       totalProd.add(myBrand);
    }
    void add(SingleProduct p, int quantity){
        String myBrand = p.getBrand();
        brands.add(myBrand);
       for (int i = 0; i < quantity; i++) {
           singlesProd.add(myBrand);
           totalProd.add(myBrand);
       }
    }
    void add (BoxedProduct p) {
        String boxedBrand = p.getBrand();
        brands.add(boxedBrand);
        boxedProd.add(boxedBrand);
        totalProd.add(boxedBrand);
    }
    void add (BoxedProduct p, int quantity) {
        String boxedBrand = p.getBrand();
        brands.add(boxedBrand);
        boxedProd.add(boxedBrand);
        
        // For total
        for(int x = 0; x < quantity; x++) {
            totalProd.add(boxedBrand);
        }
    }
    BoxedProduct[] getBoxes(String brand) {
        // Counts the frequency of boxed product objects of a brand and returns it.
        int count = Collections.frequency(boxedProd, brand);
        BoxedProduct[] getBoxed = new BoxedProduct[count];
        return getBoxed;
    }
    SingleProduct[] getSingles(String brand) {
        // Counts the frequency of single product objects of a brand and returns it.
        int count = Collections.frequency(singlesProd, brand);
        SingleProduct[] getSingle = new SingleProduct[count];
        return getSingle;
    }
    
    // Sir I added total method because I can't think of any other way to return the total for each brand.
    String[] getTotal(String brand) {
        // Counts the frequency of brands in an array and returns it.
        int count = Collections.frequency(totalProd, brand);
        String[] Total = new String[count];
        return Total;
    }
    String[] getBrands() {
        // Sets the value of brandList
        brandList = brands.toArray(brandList);
        
        // Create new arraylist for brandList Array
        ArrayList<String> newArray = new ArrayList<>();
        
        // Loop through array to remove duplicates and leave one copy of brand name
        for (int f = 0; f < brandList.length; f++) {
            if(!newArray.contains(brandList[f])) {
                newArray.add(brandList[f]);
            }
        }
        
        // Convert list back to array for the return value
        brandList = newArray.toArray(new String[newArray.size()]);
        
        return brandList;
    }

}
