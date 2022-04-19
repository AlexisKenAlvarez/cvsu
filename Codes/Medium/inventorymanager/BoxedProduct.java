/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inventorymanager;

/**
 *
 * @author ASUS
 */
public class BoxedProduct {
    String Brand;
    int Quantity;
    
    BoxedProduct(String brand, int quantity) {
        Brand = brand;
        Quantity = quantity;
    }
    String getBrand() {
        return Brand.trim(); // TRIM TO REMOVE TRAILING WHITE SPACE FROM START AND END OF THE BRAND. (Avoid space sensitive inputes)
    }
    
    int getQuantity() {
        return Quantity;
    }

}