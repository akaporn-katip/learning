package com.katipwork.learnclassobject

import org.junit.jupiter.api.Test

class TapeDeckTest {

    @Test
    fun runTapeDeckTest() {
        var t = TapeDeck()
        t.hasRecorder = true
        
        t.playTape()

        t.recordTape()
    }
}