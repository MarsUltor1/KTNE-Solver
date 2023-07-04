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
            Console.WriteLine("Welcome To Bombsolver\nPlease fill out basic information and continue to the solver");
            Console.WriteLine("\n----------------------------------------");

            // run config
            Config(ref serialNumber, ref numBatteries);

            // Loop main body
            do
            {
                // Get input
                Console.WriteLine("----------------------------------------\n\n\n----------------------------------------");
                Console.Write("Please enter a command: ");
                userIn = Console.ReadLine().ToLower();

                // Run correct function
                switch (userIn)
                {
                    case "whos on first":
                        Modules.WhosOnFirst();
                        break;

                    case "simple wires":
                        Modules.SWires();
                        break;

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
        static void Config(ref string sn, ref int nb)
        {
            // Get Serial Number
            Console.Write("Input Serial Number: ");
            sn = Console.ReadLine().ToLower();

            // Get Num Batteries
            Console.Write("Input Number of Batteries: ");
            nb = int.Parse(Console.ReadLine());

            // Print out Conformation
            Console.WriteLine($"Serial Updated to: {sn}");
            Console.WriteLine($"Number of Batteries Updated to: {nb}");
        }
    }
}