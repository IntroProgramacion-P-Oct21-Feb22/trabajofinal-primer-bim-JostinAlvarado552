/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package problema02;

import java.util.Locale;
import java.util.Scanner;

/**
 *
 * @author USUARIO 2021
 */
public class Problema02 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        //En un almacén de venta de trajes, si se compra uno se hace el 20% de 
        //descuento, si se compran 2, el 25%, si se compran 3, el 40%, y si compra 
        //más de 3, el 50%.Elaborar un algoritmo que lea la cantidad de trajes y 
        //el precio unitario (todos tienen el mismo precio) e imprima el 
        //subtotal por pagar, el descuento y el total por pagar.
   Scanner entrada = new Scanner(System.in);
        entrada.useLocale(Locale.US);
        double precio;
        int cantidad;
        double costoparcial;
        double porcentaje1 = 20;
        double porcentaje2 = 25;
        double porcentaje3 = 40;
        double porcentaje4 = 50;
        double descuento1;
        double descuento2;
        double descuento3;
        double descuento4;
        double costofinal = 0;

        System.out.println("Ingrese el costo unitario del producto");
        precio = entrada.nextDouble();
        System.out.println("Ingrese la cantidad que desea de este producto");
        cantidad = entrada.nextInt();

        costoparcial = (precio * cantidad);
        descuento1 = (costoparcial * porcentaje1) / 100;
        descuento2 = (costoparcial * porcentaje2) / 100;
        descuento3 = (costoparcial * porcentaje3) / 100;
        descuento4 = (costoparcial * porcentaje4) / 100;

        System.out.println("");
        System.out.printf("Venta de Trajes\nCantidad de productos:%d\nCosto de "
                + "los productos:%.2f\nSubtotal:%.2f\n", cantidad, precio, 
                costoparcial);
        
        if (cantidad < 0) {
            System.out.println("Valor fuera de rango");
        } else {
            if (cantidad == 1){
                costofinal = costoparcial - descuento1;
                System.out.printf("Descuento:%.2f\n", descuento1);
            } else {
                if (cantidad == 2) {
                    costofinal = costoparcial - descuento2;
                    System.out.printf("Descuento:%.2f\n", descuento2);
                } else {
                    if (cantidad == 3) {
                        costofinal = costoparcial - descuento3;
                        System.out.printf("Descuento:%.2f\n", descuento3);
                    } else {
                        if (cantidad > 3) {
                            costofinal = costoparcial - descuento4;
                            System.out.printf("Descuento:%.2f\n", descuento4);
                        }
                    }

                }
            }
        }
        System.out.printf("Costo final de venta:%.2f\n", costofinal);
        
    }
}

    
    
   
    

