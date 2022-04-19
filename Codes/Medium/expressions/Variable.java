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
public class Variable extends Expression{
    String name;
    int value;
    
    Variable(String name) {
        this.name = name;
    }
    
    Variable(String name, Integer value) {
        this.name = name;
        this.value = value;
    }
    
    String getName(){
        return name;
    }
    
    void setValue(Integer value) {
        this.value = value;
    }
    
    @Override
    Integer getValue() {
        if (value == 0) {
            return null;
        } else {
            return value;
        }
    }
    
    @Override
    public String toString() {
        return name;
    }
}
