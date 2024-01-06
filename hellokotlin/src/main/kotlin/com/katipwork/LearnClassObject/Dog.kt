package com.katipwork.LearnClassObject

class Dog (var weight: Int){
    fun bark() {
        println(if(weight < 10) "Yip!" else "Woof!")
    }
}