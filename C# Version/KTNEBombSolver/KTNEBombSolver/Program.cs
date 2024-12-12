namespace KTNEBombSolver
{
    class Program
    {
        static void Main(string[] args)
        {
            Modules modules = new Modules();
            string userIn = "";
            int lastSerial = int.MinValue;
            bool hasVowel;
            int numBatteries = int.MinValue;
            string commands = "sw (simple wires) | btn (button) | kp (keypad) | wof (whos on first) | quit";

            // Introduce the player
            Console.WriteLine("Welcome To \"Keep talking and Nobody Explodes\" Bombsolver, Console Version 0.0.2");

            // run config
            //Config(ref serialNumber, ref numBatteries);

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
        /// Setup serial number and number of buttons
        /// on the bomb
        /// </summary>
        /// <param name="sn">serial number of bomb</param>
        /// <param name="nb">number of batteries</param>
        //static void Config(ref string sn, ref int nb)
        //{
        //    // Get Serial Number
        //    Console.Write("Input Serial Number: ");
        //    sn = Console.ReadLine().ToLower();

        //    // Get Num Batteries
        //    Console.Write("Input Number of Batteries: ");
        //    nb = int.Parse(Console.ReadLine());

        //    // Print out Conformation
        //    Console.WriteLine($"Serial Updated to: {sn}");
        //    Console.WriteLine($"Number of Batteries Updated to: {nb}");
        //}
    }
}