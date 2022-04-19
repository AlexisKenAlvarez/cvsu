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
public class Negation extends unaryOperation{
    int val;

    public Negation(Expression operand) {
        super(operand);
    }
    
    @Override
    Integer getValue() {
        if (p2 == null) {
            return null;
        } else {
            if (operand < 0) {
            
            int newVal = Math.abs(operand);
            this.val = newVal;
            
            return val;
        } 
            else if (operand > 0){
            this.val = (~(operand - 1));
            
            return val;
            }
        }
        return null;
    }

    @Override
    public String toString() {
        if (operand == 0) {
            char ch = name.charAt(0);
            if (ch == '-') {
                return name.substring(1);
            } else {
                return "-" + name;
            }
        } else {
            return Integer.toString(val);
        }
        
       
        
    }
}
