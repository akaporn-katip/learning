package com.katipwork.learnclassobject

import org.junit.jupiter.api.Test
class DogTest {

    @Test
    fun barkTest() {
        var dog = Dog("Fido", 10, "Mixed")

        println(dog.name)
        dog.bark()

        var dogs = arrayOf(Dog("Fido", 10, "Mixed"))

        println("There are ${dogs.size} dogs.")


        println(dog.weightInKgs)
    }
}