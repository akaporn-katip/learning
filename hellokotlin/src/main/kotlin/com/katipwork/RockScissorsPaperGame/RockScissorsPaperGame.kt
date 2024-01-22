package com.katipwork.rockscissorspapergame
fun runGame() {
    for(i in 1..3) {
        val computer = getGameChoice()
        val player = getUserChoice()
        val result = getGameResult(computer, player)
        println("Computer choose: $computer,\nPlayer choose: $player,\nResult: ${printResult(result)}\n")
    }
}

fun getGameChoice() = getChoice()[((Math.random() * getChoice().size) + 0).toInt()]

fun getChoice(): Array<String> {
    return arrayOf("Rock", "Scissors", "Paper")
}

fun getUserChoice() : String {
    while (true) {
        print("Please enter one of following: ${getChoice().joinToString(" ")} : ")
        val result = readln().trim()
        if (result in getChoice()) {
            return result
        }
        println("Errr...dunno")
        println("You must enter a valid choice.\n")
    }
}

fun getGameResult(computer: String, player: String) : Int {
    return if (computer == "Scissors" && player == "Paper") -1
    else if (computer == "Rock" && player == "Scissors") -1
    else if (computer == "Paper" && player == "Rock") -1
    else if (computer == player) 0
    else 1
}
fun printResult(result: Int) : String {
    return when (result) {
       -1 -> "Computer wins!!!"
        0 -> "Draw!!!"
        else -> "You wins!!!"
    }
}