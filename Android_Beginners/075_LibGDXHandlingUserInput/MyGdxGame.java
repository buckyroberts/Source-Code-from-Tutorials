package com.thenewboston.buckyblaster;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

public class MyGdxGame extends ApplicationAdapter implements InputProcessor {

    private SpriteBatch batch;

    //Screen dimensions will be used to center text
    private BitmapFont font;
    private int screenWidth, screenHeight;
    private String message = "Touch me";

    //Set screen dimensions, font, and use this class for input processing
    @Override
    public void create () {
        batch = new SpriteBatch();

        screenWidth = Gdx.graphics.getWidth();
        screenHeight = Gdx.graphics.getHeight();

        font = new BitmapFont();
        font.setColor(Color.BLUE);
        font.scale(5);

        Gdx.input.setInputProcessor(this);
    }

    //Don't forget to free font
    @Override
    public void dispose() {
        batch.dispose();
        font.dispose();
    }

    //Get middle of screen and adjust for message size
    @Override
    public void render () {
        Gdx.gl.glClearColor(1,1,1,1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        BitmapFont.TextBounds textSize = font.getBounds(message);
        float x = screenWidth/2 - textSize.width/2;
        float y = screenHeight/2 + textSize.height/2;

        batch.begin();
        font.draw(batch, message, x, y);
        batch.end();
    }

    //Return true to indicate that the event was handled
    @Override
    public boolean touchDown(int screenX, int screenY, int pointer, int button) {
        message = "Touched down at " + screenX + ", " + screenY;
        return true;
    }

    //When finger is lifted up
    @Override
    public boolean touchUp(int screenX, int screenY, int pointer, int button) {
        message = "Touch up at " + screenX + ", " + screenY;
        return true;
    }

    //While dragging finger across screen
    @Override
    public boolean touchDragged(int screenX, int screenY, int pointer) {
        message = "Dragging at " + screenX + ", " + screenY;
        return true;
    }

    @Override
    public boolean keyDown(int keycode) {
        return false;
    }

    @Override
    public boolean keyUp(int keycode) {
        return false;
    }

    @Override
    public boolean keyTyped(char character) {
        return false;
    }

    @Override
    public boolean mouseMoved(int screenX, int screenY) {
        return false;
    }

    @Override
    public boolean scrolled(int amount) {
        return false;
    }
    
}