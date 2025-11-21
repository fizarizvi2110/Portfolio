import java.awt.*;
import javax.swing.*;

public class DrawTicTacToe extends Canvas
{
    public int xRow, xCol;
    public int oRow, oCol;

    public void paint(Graphics g)
    {
        g.setColor(Color.BLACK);
        // Vertical Lines
        g.drawLine(150, 50, 150, 350);
        g.drawLine(250, 50, 250, 350);
        // Horiztonal Lines
        g.drawLine(50, 150, 350, 150);
        g.drawLine(50, 250, 350, 250);
        //Draw & Place X's on Row 0
        if (xRow == 0){
            g.setColor(Color.RED);
            g.drawLine(65 + (100*xCol), 65, 135 + (100*xCol), 135);
            g.drawLine(135 + (100*xCol), 65, 65 + (100*xCol), 135);
        }
        if (xRow == 1){
            g.setColor(Color.RED);
            g.drawLine(65 + (100*xCol), 165, 135 + (100*xCol), 235);
            g.drawLine(135 + (100*xCol), 235, 65+(100*xCol), 235);
        }
        if (xRow == 2){
            g.setColor(Color.RED);
            g.drawLine(65+(100*xCol), 265, 135+(100*xCol), 335);
            g.drawLine(135+(100*xCol), 265, 65+(100*xCol), 335);
        }
            //Draw & Place O's
        if (oRow == 0){
            g.setColor(Color.BLUE);
            g.drawOval(65+(100*oCol), 65, 75, 75);
        }
        if (oRow == 1){
            g.setColor(Color.BLUE);
            g.drawOval(65+(100*oCol), 165, 75, 75);
        }
        if (oRow == 2){
            g.setColor(Color.BLUE);
            g.drawOval(65+(100*oCol), 265, 75, 75);
        }
    }        

    public static void main(String[] args)
    {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        DrawTicTacToe drawing = new DrawTicTacToe();
        drawing.xRow = Integer.parseInt(args[0]);
        drawing.xCol = Integer.parseInt(args[1]);
        drawing.oRow = Integer.parseInt(args[2]);
        drawing.oCol = Integer.parseInt(args[3]);
        drawing.setSize(400, 400);
        frame.add(drawing);
        frame.pack();
        frame.setVisible(true);
    }
}