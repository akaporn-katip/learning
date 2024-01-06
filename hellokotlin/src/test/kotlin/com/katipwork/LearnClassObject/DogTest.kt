package com.katipwork.LearnClassObject

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

class DogTest {

    @Test
    fun barkTest() {
        var dog: Dog = Dog(10)
        dog.bark()
    }
}