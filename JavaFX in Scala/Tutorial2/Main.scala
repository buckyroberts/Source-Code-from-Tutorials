package Tutorial2

/**
 * Created by xxc3nsoredxx on 1/2/2016.
 */

import javafx.application.Application
import javafx.event.{ActionEvent, EventHandler}
import javafx.scene.control.Button
import javafx.scene.layout.StackPane
import javafx.scene.Scene
import javafx.stage.Stage

import scala.annotation.switch

class Main extends Application with EventHandler[ActionEvent] {
    val button = new Button()
    val layout = new StackPane()
    val scene = new Scene(layout, 300, 250)

    override def start(primary_stage: Stage) {
        primary_stage.setTitle("Title of the Window")

        button.setText("Click me")
        button.setOnAction(this)

        layout.getChildren.add(button)

        primary_stage.setScene(scene)

        primary_stage.show()
    }

    override def handle(event: ActionEvent): Unit = {
        //Used a switch because it's easier to expand than if-else
        //Might as well start it now
        (event.getSource: @switch) match {
            case button => println("OOooooo i love it when you touch me there.....")
        }
    }
}