package com.katipwork.learnclassobject

import com.katipwork.learnclassobject.Song
import org.junit.jupiter.api.Test

class SongTest {

    @Test
    fun songPlayerTest() {
        val song: Song = Song("Bohemian Rhapsody", "Queen")
        song.play()
        song.stop()
        song.play()
    }
}