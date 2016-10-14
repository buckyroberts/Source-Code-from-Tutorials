package com.thenewboston.buckyblaster;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.GlyphLayout;

/* Get Bound has been depricated in newer Version. Use glyphLayout Instead*/
public class MyGdxGame extends ApplicationAdapter implements InputProcessor {

    private SpriteBatch batch;

    //Screen dimensions will be used to center text
    private BitmapFont font;
    private int screenWidth, screenHeight;
    private String message = "Touch me";
    private GlyphLayout layout;

    //Set screen dimensions, font, and use this class for input processing
    @Override
    public void create () {
        batch = new SpriteBatch();
        
        layout = new GlyphLayout();
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

        
        glyphLayout.setText(font, message);
        BitmapFont.TextBounds textSize = font.getBounds(message);
      

        batch.begin();
        font.draw(batch, glyphLayout, screenWidth/2 - glyphLayout.width/2, screenHeight/2 + glyphLayout.height/2);
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
