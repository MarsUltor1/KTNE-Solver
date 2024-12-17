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

            int numBatteries = int.MinValue;
            bool numBatteriesSet = false;

            bool hasVowel = false;
            bool hasVowelSet = false;

            bool parallelPort = false;
            bool parallelPortSet = false;

            int numStrikes = 0;
            
            string commands = "sw (simple wires) | btn (button) | kp (keypad) | ss (simon says) | wof (whos on first) | mem (memory) | mc (morse code) | cw (complicated wires) | ws (wire sequences) | quit";

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
                        // Check that all prerequisites are setup
                        SetLastSerial(ref lastSerial, ref lastSerialSet);

                        // Call module solving function
                        modules.SWires(lastSerial);
                        break;

                    case "btn":
                        // Check that all prerequisites are setup
                        SetNumBatteries(ref numBatteries, ref numBatteriesSet);

                        // Call module solving function
                        modules.Button(numBatteries);
                        break;

                    case "kp":
                        modules.Keypad();
                        break;

                    case "ss":
                        // Check that all prerequisites are setup
                        if (!hasVowelSet) SetVowel(ref hasVowel, ref hasVowelSet);
                        CheckNumStrikes(ref numStrikes);

                        // Call module solving function
                        modules.SimonSays(hasVowel, numStrikes);
                        break;

                    case "wof":
                        modules.WhosOnFirst();
                        break;

                    case "mem":
                        modules.Memory();
                        break;

                    case "mc":
                        modules.MorseCode();
                        break;

                    case "cw":
                        // Check that all prerequisites are setup
                        SetLastSerial(ref lastSerial, ref lastSerialSet);
                        SetNumBatteries(ref numBatteries, ref numBatteriesSet);
                        SetParallel(ref parallelPort, ref parallelPortSet);

                        // Call module solving function
                        modules.ComplicatedWires(lastSerial, parallelPort, numBatteries);
                        break;

                    case "ws":
                        modules.WireSequences();
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
        /// Set what the last serial number of the bomb is if not alread set
        /// </summary>
        /// <param name="lastSerial">What is the last digit of the serial number</param>
        /// <param name="lastSerialSet">Has the lastSerial int already been set</param>
        public static void SetLastSerial(ref int lastSerial, ref bool lastSerialSet)
        {
            // check that vowel hasn't already been set
            if (lastSerialSet) return;

            // set the has vowel boolean based on user input
            while (true)
            {
                Console.Write("\nWhat is the last digit of the serial number: ");
                if (int.TryParse(Console.ReadLine().ToLower().Trim(), out lastSerial))
                {
                    lastSerialSet = true;
                    return;
                }
                else
                {
                    continue;
                }
            }
        }

        /// <summary>
        /// Set how many batteries the bomb has if it hasn't already been set
        /// </summary>
        /// <param name="numBatteries">how many batteries does the bomb have</param>
        /// <param name="numBatteriesSet">Has the numBatteries int already been set</param>
        public static void SetNumBatteries(ref int numBatteries, ref bool numBatteriesSet)
        {
            // check that vowel hasn't already been set
            if (numBatteriesSet) return;

            // set the has vowel boolean based on user input
            while (true)
            {
                Console.Write("\nHow many batteries does the bomb have: ");
                if (int.TryParse(Console.ReadLine().ToLower().Trim(), out numBatteries))
                {
                    numBatteriesSet = true;
                    return;
                }
                else
                {
                    continue;
                }
            }
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
                Console.Write("\nDose the serial number contain a vowel (Y/N): ");
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
        
        /// <summary>
        /// Set whether the bomb has a parallel port or not if it is not already set
        /// </summary>
        /// <param name="hasParallel">Does the bomb have a parallel port</param>
        /// <param name="hasParallelSet">Has the hasParallel bool already been set</param>
        public static void SetParallel (ref bool hasParallel, ref bool hasParallelSet)
        {
            // check that vowel hasn't already been set
            if (hasParallelSet) return;

            // set the has vowel boolean based on user input
            while (true)
            {
                Console.Write("\nDose the bomb have a parallel port (Y/N): ");
                string input = Console.ReadLine().ToLower().Trim();

                if (input == "y")
                {
                    hasParallel = true;
                    hasParallelSet = true;
                }
                else if (input == "n")
                {
                    hasParallel = false;
                    hasParallelSet = true;
                }
                else
                {
                    Console.WriteLine("ERROR: invalid input please try again.");
                    continue;
                }

                break;
            }
        }

        /// <summary>
        /// Checks that the number of strikes hasn't changed if a module depends on it
        /// </summary>
        /// <param name="numStrikes">number of strikes on the bomb</param>
        public static void CheckNumStrikes (ref int numStrikes)
        {
            // Check if the number or strikes has even changed
            Console.Write($"\nIs the bomb still at {numStrikes} strikes (Y/N) ");
            string input = Console.ReadLine().ToLower().Trim();
            if (input == "y") return;

            // If number of strikes is different get the new number
            while (true)
            {
                Console.Write($"How many strikes are on the bomb (0, 1, 2) ");
                input = Console.ReadLine().ToLower().Trim();
                switch (input) 
                {
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