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
public abstract class unaryOperation extends Expression{
    
    int operand;
    String name;
    Expression p2;
    
    
    
    unaryOperation (Expression operand) {
        if (operand.getValue() == null) {
            this.operand = 0;

        } else if (operand.getValue() == 0) {
            this.operand = 0;
        }
        else {
            this.operand = operand.getValue();
        }
        this.name = operand.toString();
        this.p2 = operand;
        
        
    }
    
    final Expression getOperand() {
        return p2;
    }
    

}
