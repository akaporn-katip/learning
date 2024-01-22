package com.katipwork.learnclassobject

public class Dog (val name_param: String, var weight_param: Int, val breed_param: String) {
    val name = name_param
    var weight = weight_param
        set(value) {
            if (value > 0) field = value
//            if (value > 0) weight = value // Don't do this! You'll get stuck in an endless loop. Use field instead.
        }

    val weightInKgs: Double
        get() = weight / 2.2

    var temperament: String
    lateinit var temp: String
//    lateinit var numb: Int // lateinit can't use it with any of the following types: Byte, Short, Int, Long, Double, Float, Char or Boolean

    init {
        println("Dog $name has been created.")
        temperament = ""
    }

    init {
        println("Dog weight is $weight ")
    }

    val breed = breed_param.uppercase()
    var activities = arrayOf("walks")

    init {
        println("The breed is $breed.")
    }

    fun bark() {
        println(if(weight < 10) "Yip!" else "Woof!")
    }
}