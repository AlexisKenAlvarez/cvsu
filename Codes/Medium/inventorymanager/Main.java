package inventorymanager;
/**
 *
 * @author Alexis Ken Alvarez // ASUS ROG
 */
import java.util.Arrays;
import java.util.Scanner;
public class Main {

    @SuppressWarnings("empty-statement")
    public static void main(String[] args) {
        Scanner obj = new Scanner(System.in);
 
        // Boolean to keep the loop running until condition is met.
        boolean cond = true;
        
        // Inventory Object
        InventoryManager inv = new InventoryManager();

        // Input prompt
        while (cond == true) {
            System.out.print("Options: \n\t[1] Add Single Product\n\t[2] Add Box Product\n\t[3] Exit\n");
            System.out.print("Choice: ");
            int choice = obj.nextInt();
            
            obj.nextLine();
            switch (choice) {
                case 1:
                    System.out.print("Brand: ");
                    String sBrand = obj.nextLine();
                    
                    System.out.print("Quantity: ");
                    int sQuan = obj.nextInt();
                    
                    obj.nextLine();
                    SingleProduct brand = new SingleProduct(sBrand);
                    
                    if (sQuan > 1) {
                        inv.add(brand, sQuan);
                    } else {
                        inv.add(brand);
                    }
                    break;
                case 2:
                    System.out.print("Brand: ");
                    String bBrand = obj.nextLine();
                    
                    System.out.print("Items in box: ");
                    int items = obj.nextInt();
                    
                    System.out.print("Quantity: ");
                    int bQuan = obj.nextInt();
                    obj.nextLine();
                    
                    BoxedProduct bProd = new BoxedProduct(bBrand, items);
                    
                    if(bQuan == 1) {
                        if (bProd.getQuantity() == 1) {
                            inv.add(bProd);
                        } else if (bProd.getQuantity() > 1) {
                            inv.add(bProd, bProd.getQuantity());
                        }
                    } else if (bQuan > 1){
                        for(int x = 0; x < bQuan; x++) {
                            int newCount = bProd.getQuantity(); 
                            inv.add(bProd, newCount);
                        }
                    }
                    break;
                case 3:
                    // OUTPUT
                    System.out.println("\n");
                    System.out.println("--INVENTORY REPORT--");
                    System.out.println("\n");
                   
                    // GET Brands
                    String[] brandArrays = inv.getBrands();
                    
                    // LOOP THROUGH THE NUMBER OF BRANDS IN THE INVENTORY
                    for(int i = 0; i < inv.getBrands().length; i++) {
                        
                        // VALUES OF SINGLES, BOXES, AND TOTAL OF BRANDS IN A STRING TO COUNT NUMBER OF  NULL VALUE.
                        String singles = Arrays.toString(inv.getSingles(brandArrays[i]));
                        String Total = Arrays.toString(inv.getTotal(brandArrays[i]));
                        String boxed = Arrays.toString(inv.getBoxes(brandArrays[i]));

                        // The values SinglesArray, boxedArray, and total returns correct value but presents null, so I decided to split the null words and get their lengths to get the value in number.
                        System.out.println(brandArrays[i]);
                        System.out.println("\tSingles: " + singles.split(",").length);
                        System.out.println("\tBoxed: " + boxed.split(",").length);
                        System.out.println("\tTotal Pieces: " + Total.split(",").length);
                        System.out.println("\n");
                    }       cond = false;
                    break;
                default:        
                    break;
            }
            }
    } 
}
