package Tutorial3

/**
 * Created by xxc3nsoredxx on 1/2/2016.
 */

import javafx.application.Application
import javafx.event
import javafx.event.{EventHandler, ActionEvent}
import javafx.scene.control.Button
import javafx.scene.layout.StackPane
import javafx.scene.{Scene, Parent}
import javafx.stage.Stage

import scala.annotation.switch

class Main extends Application {
    val button = new Button()
    val layout = new StackPane()
    val scene = new Scene(layout, 300, 250)

    override def start(primary_stage: Stage) {
        primary_stage.setTitle("Title of the Window")

        button.setText("Click me")
        //Handles button events with anonymous inner class
        button.setOnAction(new EventHandler[ActionEvent] {
            override def handle(event: ActionEvent): Unit = println("I'm an anonymous inner class")
        })

        //I couldn't get lambda to work so I opted to leave it out
        //Besides, doing it the way above isn't so bad

        layout.getChildren.add(button)

        primary_stage.setScene(scene)

        primary_stage.show()
    }
}