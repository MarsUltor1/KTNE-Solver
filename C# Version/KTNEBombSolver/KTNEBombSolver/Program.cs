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
                    Console.Write("Word: ");
                    string decrypt = 
                }
                #endregion
            }
        }
    }
}