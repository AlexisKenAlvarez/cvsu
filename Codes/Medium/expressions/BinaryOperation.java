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
public abstract class BinaryOperation extends Expression{
    int leftOperand, rightOperand;
    String name;
    
    Expression p1, p2;
    
    BinaryOperation (Expression leftOperand, Expression rightOperand) {
        if (leftOperand.getValue() == null) {
            this.name = leftOperand.toString();
        } else {
            this.leftOperand = leftOperand.getValue();
        }
        
        if (rightOperand.getValue() == null) {
            this.name = rightOperand.toString();
        } else {
            this.rightOperand = rightOperand.getValue();

        }

        this.p1 = leftOperand;
        this.p2 = rightOperand;
    }
    
    final Expression getLeftOperand() {
        return p1;
    }
    
    final Expression getRightOperand() {
        return p2;
    }
}
