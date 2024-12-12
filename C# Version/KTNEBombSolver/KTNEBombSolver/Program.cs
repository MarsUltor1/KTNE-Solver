namespace KTNEBombSolver
{
    class Program
    {
        static void Main(string[] args)
        {
            Modules modules = new Modules();
            string userIn = "";

            int lastSerial = int.MinValue;
            bool lastSerialSet = false;

            bool hasVowel = false;
            bool hasVowelSet = false;

            int numStrikes = 0;

            int numBatteries = int.MinValue;
            bool numBatteriesSet = false;

            string commands = "sw (simple wires) | btn (button) | kp (keypad) | ss (simon says) | wof (whos on first) | quit";

            // Introduce the player
            Console.WriteLine("Welcome To \"Keep talking and Nobody Explodes\" Bombsolver, Console Version 0.0.2");

            // Loop main body
            do
            {
                // Get input
                Console.WriteLine("----------------------------------------\n\n\n----------------------------------------");
                Console.WriteLine("The available commands are:\n" + commands);
                Console.Write("\nPlease enter a command: ");
                userIn = Console.ReadLine().ToLower();

                // Run correct function
                switch (userIn)
                {
                    case "sw":
                        modules.SWires(ref lastSerial);
                        break;

                    case "btn":
                        modules.Button(ref numBatteries);
                        break;

                    case "kp":
                        modules.Keypad();
                        break;

                    case "ss":
                        // Check that all prerequisites are setup
                        if (!hasVowelSet) SetVowel(ref hasVowel, ref hasVowelSet);
                        CheckNumStrikes(ref numStrikes);

                        // Call module solving function
                        modules.SimonSays(ref hasVowel, ref numStrikes);
                        break;

                    case "wof":
                        modules.WhosOnFirst();
                        break;

                    case "quit":
                        Console.WriteLine("Thank you for playing! Come again.");
                        Console.WriteLine("----------------------------------------");
                        break;

                    default:
                        Console.WriteLine("Invalid Command, Please try Again");
                        break;
                }
            }
            while (userIn != "quit");
        }

        /// <summary>
        /// Set up the has value boolean and mark its has set bool to true
        /// </summary>
        /// <param name="hasVowel">reference to boolean that tracks whether the serial number contains a vowel</param>
        /// <param name="hasVowelSet">has the hasVowel bool been set already</param>
        public static void SetVowel (ref bool hasVowel, ref bool hasVowelSet)
        {
            // check that vowel hasn't already been set
            if (hasVowelSet) return;

            // set the has vowel boolean based on user input
            while (true)
            {
                Console.Write("\nDose the serial number contain a vowel, y (yes) n (no) ");
                string input = Console.ReadLine().ToLower().Trim();

                if (input == "y")
                {
                    hasVowel = true;
                    hasVowelSet = true;
                }
                else if (input == "n")
                {
                    hasVowel = false;
                    hasVowelSet = true;
                }
                else
                {
                    Console.WriteLine("ERROR: invalid input please try again.");
                    continue;
                }

                break;
            }
        }

        public static void CheckNumStrikes (ref int numStrikes)
        {
            while (true)
            {
                Console.Write($"\nIs the bomb still at {numStrikes} strikes.\nEnter: y (yes) or 0, 1, or 2 if it is at a different number of stirkes ");
                string input = Console.ReadLine().ToLower().Trim();

                switch (input) 
                {
                    case "y": return;
                    case "0": numStrikes = 0; return;
                    case "1": numStrikes = 1; return;
                    case "2": numStrikes = 2; return;

                    default:
                        Console.WriteLine("ERROR: invalid input please try again");
                        break;
                }
            }
        }
    }
}