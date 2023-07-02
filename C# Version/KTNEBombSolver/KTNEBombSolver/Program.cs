namespace KTNEBombSolver
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string userIn = "";
            string serialNumber = "";
            int numBatteries = 0;

            // Introduce the player
            Console.WriteLine("Welcome To Bombsolver\nPlease fill out basic information and continue to the solver\n");

            // run config
            Config(serialNumber, numBatteries);

            // Loop main body
            do
            {
                // Get input
                Console.Write("\nPlease enter a command: ");
                userIn = Console.ReadLine().ToLower();

                // Run correct function
                switch (userIn)
                {
                    case "quit":
                        Console.WriteLine("Thank you for playing! Come again.");
                        break;
                    default:
                        Console.WriteLine("Invalid Command, Please try Again");
                        break;
                }
            }
            while (userIn != "quit");
        }

        /// <summary>
        /// Setup serial number and number of buttons
        /// on the bomb
        /// </summary>
        /// <param name="sn">serial number of bomb</param>
        /// <param name="nb">number of batteries</param>
        static void Config(string sn, int nb)
        {
            // Get Serial Number
            Console.Write("Input Serial Number: ");
            sn = Console.ReadLine().ToLower();

            // Get Num Batteries
            Console.Write("Input Number of Batteries: ");
            nb = int.Parse(Console.ReadLine());

            // Print out Conformation
            Console.WriteLine($"\nSerial Updated to: {sn}");
            Console.WriteLine($"Number of Batteries Updated to: {nb}");
        }

        static void WhosOnFirst()
        {
            // Trackers
            bool located = false;
            bool decrypted = false;
            int stage = 1;

            while (stage <= 3)
            {
                #region Locate Word
                while (!located)
                {
                    // Get Word on Display
                    Console.Write("Word on Display: ");
                    string locate = Console.ReadLine().ToLower();

                    // Figure out Position to Look
                    if (locate == "" || locate == "leed" || locate == "reed" || locate == "they're")
                    {
                        Console.WriteLine("Bottom Left");
                        located = true;
                        decrypted = false;
                    }
                    else if (locate == "cee" || locate == "display" || locate == "hold on" || locate == "lead" || locate == "no" || locate == "says" || locate == "see" || locate == "there" || locate == "you are")
                    {
                        Console.WriteLine("Bottom Right");
                        located = true;
                        decrypted = false;
                    }
                    else if (locate == "led" || locate == "nothing" || locate == "they are" || locate == "yes")
                    {
                        Console.WriteLine("Middle Left");
                        located = true;
                        decrypted = false;
                    }
                    else if (locate == "blank" || locate == "read" || locate == "red" || locate == "their" || locate == "you" || locate == "you're" || locate == "your")
                    {
                        Console.WriteLine("Middle Right");
                        located = true;
                        decrypted = false;
                    }
                    else if (locate == "ur")
                    {
                        Console.WriteLine("Upper Left");
                        located = true;
                        decrypted = false;
                    }
                    else if (locate == "c" || locate == "okay" || locate == "first")
                    {
                        Console.WriteLine("Upper Right");
                        located = true;
                        decrypted = false;
                    }
                    else
                    {
                        Console.WriteLine("ERROR: Invalid Word, Try Again. Enter [X] To Quit. Enter [C] to continue.");
                        string cont = Console.ReadLine().ToLower();

                        if (cont == "x")
                        {
                            located = true;
                            decrypted = true;
                            stage = 4;
                        }
                    }
                }
                #endregion

                #region Decrypt Word
                while (!decrypted)
                {
                    // Get Word on Button
                    Console.Write("Word: ");
                    string decrypt = Console.ReadLine().ToLower();

                    // Get String of Words
                    switch(decrypt)
                    {
                        case "blank":
                            Console.WriteLine("WAIT, RIGHT, OKAY, MIDDLE, BLANK");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "done":
                                    print("SURE, UH HUH, NEXT, WHAT? YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE")
                            decrypted = True
                            stage += 1
                            located = False
                        case "first":
                                    print("LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST")
                            decrypted = True
                            stage += 1
                            located = False
                        case "hold":
                                    print("YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD")
                            decrypted = True
                            stage += 1
                            located = False
                        case "left":
                                    print("RIGHT, LEFT")
                            decrypted = True
                            stage += 1
                            located = False
                        case "like":
                                    print("YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE")
                            decrypted = True
                            stage += 1
                            located = False
                        case "middle":
                                    print("BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE")
                            decrypted = True
                            stage += 1
                            located = False
                        case "next":
                                    print("WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT")
                            decrypted = True
                            stage += 1
                            located = False
                        case "no":
                                    print("BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO")
                            decrypted = True
                            stage += 1
                            located = False
                        case "nothing":
                                    print("UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING")
                            decrypted = True
                            stage += 1
                            located = False
                        case "okay":
                                    print("MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY")
                            decrypted = True
                            stage += 1
                            located = False
                        case "press":
                                    print("RIGHT, MIDDLE, YES, READY, PRESS")
                            decrypted = True
                            stage += 1
                            located = False
                        case "ready":
                                    print("YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY")
                            decrypted = True
                            stage += 1
                            located = False
                        case "right":
                                    print("YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT")
                            decrypted = True
                            stage += 1
                            located = False
                        case "sure":
                                    print("YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE")
                            decrypted = True
                            stage += 1
                            located = False
                        case "u":
                                    print("UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U")
                            decrypted = True
                            stage += 1
                            located = False
                        case "uh huh":
                                    print("UH HUH")
                            decrypted = True
                            stage += 1
                            located = False
                        case "uh uh":
                                    print("UR, U, YOU ARE, YOU'RE, NEXT, UH UH")
                            decrypted = True
                            stage += 1
                            located = False
                        case "uhhh":
                                    print("READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH")
                            decrypted = True
                            stage += 1
                            located = False
                        case "ur":
                                    print("DONE, U, UR")
                            decrypted = True
                            stage += 1
                            located = False
                        case "wait":
                                    print("UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT")
                            decrypted = True
                            stage += 1
                            located = False
                        case "what":
                                    print("UHHH, WHAT")
                            decrypted = True
                            stage += 1
                            located = False
                        case "what?":
                                    print("YOU, HOLD, YOU'RE. YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?")
                            decrypted = True
                            stage += 1
                            located = False
                        case "yes":
                                    print("OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES")
                            decrypted = True
                            stage += 1
                            located = False
                        case "you":
                                    print("SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU")
                            decrypted = True
                            stage += 1
                            located = False
                        case "you are":
                                    print("YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE")
                            decrypted = True
                            stage += 1
                            located = False
                        case "you're":
                                    print("YOU, YOU'RE")
                            decrypted = True
                            stage += 1
                            located = False
                        case "your":
                                    print("UH UH, YOU ARE, UH HUH, YOUR")
                            decrypted = True
                            stage += 1
                            located = False
                        case _:
                                    print("ERROR: CHECK SPELLING. ENTER [X] TO QUIT. ENTER ANYTHING ELSE TO CONTINUE.")
                            cont = input()
                            cont = cont.lower()

                            if cont == "x":
                                decrypted = True
                                stage = 4
                    }
                }
                #endregion
            }
        }
    }
}