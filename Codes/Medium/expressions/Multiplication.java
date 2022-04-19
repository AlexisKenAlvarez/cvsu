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
public class Multiplication extends BinaryOperation{
    
    String left = Integer.toString(leftOperand);
    String right = Integer.toString(rightOperand);

    public Multiplication(Expression leftOperand, Expression rightOperand) {
        super(leftOperand, rightOperand);
    }
    @Override
    Integer getValue() {
        if (leftOperand == 0 || rightOperand == 0) {
            return null;
        } else 
            return leftOperand * rightOperand;
        }
    
    @Override
    public String toString() {
        if(p1.getValue() == null) {
            return "(" + name + "*" + p2.toString() + ")";
        } else if(p2.getValue() == null) {
            return "(" + p1.toString() + "*" + name + ")";
        } else {
            return "(" + p1.toString() + "*" + p2.toString() + ")";
        }
    }
        
}
    
    

