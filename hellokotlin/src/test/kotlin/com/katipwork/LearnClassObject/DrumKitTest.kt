package com.katipwork.learnclassobject

import org.junit.jupiter.api.Test

class DrumKitTest {

    @Test
    fun runDrumKit() {
        var d = DrumKit(true, true)
        d.playTopHat()
        d.playSnare()
        d.hasSnare = false;
        d.playTopHat()
        d.playSnare()
    }
}