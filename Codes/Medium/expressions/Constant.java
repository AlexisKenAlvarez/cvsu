/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package expressions;

/**
 *
 * @author ASUS
 */
public class Constant extends Expression{
    
    int val;
    
    Constant (Integer value) {
        this.val = value;
    }
    
    @Override
    Integer getValue() {
        return val;
    }
    
    @Override
    public String toString(){
        return Integer.toString(val);
    }
    
}
