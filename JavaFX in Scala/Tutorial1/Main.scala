package Tutorial1

/**
 * Created by Echidna on 1/1/2016.
 */

import javafx.application.Application
import javafx.scene.Scene
import javafx.scene.control.Button
import javafx.scene.layout.StackPane
import javafx.stage.Stage

class Main extends Application {
    override def start(primary_stage: Stage): Unit = {
        primary_stage.setTitle("Title of the Window")

        val button = new Button()
        button.setText("Click me")

        val layout = new StackPane()
        layout.getChildren.add(button)

        val scene = new Scene(layout, 300, 250)
        primary_stage.setScene(scene)

        primary_stage.show()
    }
}