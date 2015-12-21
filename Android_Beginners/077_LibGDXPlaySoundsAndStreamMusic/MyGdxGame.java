package com.thenewboston.gamesample;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.audio.Music;
import com.badlogic.gdx.audio.Sound;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

public class MyGdxGame extends ApplicationAdapter implements InputProcessor {

    private SpriteBatch batch;
    
    //Declare sound objects
    Sound gameOverSound;
    Music clamJam;

    @Override
    public void create () {
        batch = new SpriteBatch();
        Gdx.input.setInputProcessor(this);
        
        //Initialize and set input processor
        gameOverSound = Gdx.audio.newSound(Gdx.files.internal("sounds/Death2.wav"));
        clamJam = Gdx.audio.newMusic(Gdx.files.internal("sounds/clamJam.wav"));
    }

    @Override
    public void dispose() {
        //Make sure to dispose of it
        gameOverSound.dispose();
        clamJam.dispose();
        batch.dispose();
    }

    @Override
    public void render () {
        Gdx.gl.glClearColor(1,1,1,1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);
        batch.begin();
        batch.end();
    }

    @Override
    public boolean touchDown(int screenX, int screenY, int pointer, int button) {
        //Play the sound
        //gameOverSound.play();

        //Set pitch to 50% and volume to 90%
        //long soundId = gameOverSound.play();
        //gameOverSound.setPitch(soundId,0.5f);
        //gameOverSound.setVolume(soundId,0.9f);

        //Play streaming music
        clamJam.play();
        return true;
    }

    @Override
    public boolean touchUp(int screenX, int screenY, int pointer, int button) {
        //Pauses the music, you can also stop() for starting over
        clamJam.pause();
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
    public boolean touchDragged(int screenX, int screenY, int pointer) {
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