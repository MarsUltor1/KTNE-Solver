using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;

namespace KTNEBombSolver
{
    enum Color
    {
        Red,
        Yellow,
        Blue,
        Black,
        White,
        Green,
        Null
    }

    enum Symbol
    {
        Copyright,
        FilledStar,
        HollowStar,
        SmileyFace,
        DoubleK,
        Omega,
        SquidKnife,
        Pumpkin,
        HookN,
        Six,
        SquigglyN,
        AT,
        AE,
        MeltedThree,
        Euro,
        NWithHat,
        Dragon,
        QuestionMark,
        Paragraph,
        RightC,
        LeftC,
        Pitchfork,
        Cursive,
        Tracks,
        Balloon,
        UpsideDownY,
        BT
    }

    public class Modules
    {


        /// <summary>
        /// Solve "Simple Wires" Module
        /// </summary>
        /// <param name="lastSerial">last digit of serial number</param>
        public void SWires(ref int lastSerial)
        {

            List<string> wires = new List<string>();
            List<Color> colors = new List<Color>();
            bool quit = false;

            // Get last digit of serial #
            if (lastSerial < 0)
            {
                Console.Write("\nEnter the last digit of serial #: ");
                lastSerial = int.Parse(Console.ReadLine());
            }

            #region Input Wires
            while (!quit)
            {
                // Get all wires
                Console.WriteLine("\nColors: r (red) | y (yellow | b (blue) | bl (black | w (white) ");
                Console.Write("Enter Every Wire Color: ");
                string wireString = Console.ReadLine().ToLower();

                // Add wires to list
                wires.Clear();
                wires.AddRange(wireString.Split(new char[] { ' ' }));

                // Check for correct number of wires
                if (wires.Count < 3 || wires.Count > 6)
                {
                    Console.Write("ERROR: Invalid number of wires, enter between 3 and 6 colors. Enter [C] to continue or [X] To Quit. ");
                    string cont = Console.ReadLine().ToLower();
                    if (cont == "x") quit = true;
                    continue;
                }

                // Change colors to enum
                for (int i = 0; i < wires.Count; i++)
                {
                    switch (wires[i])
                    {
                        // Handle correctly input colors
                        case "r": colors.Add(Color.Red); break;
                        case "y": colors.Add(Color.Yellow); break;
                        case "b": colors.Add(Color.Blue); break;
                        case "bl": colors.Add(Color.Black); break;
                        case "w": colors.Add(Color.White); break;

                        // Send error message for incorrectly input colors
                        default:
                            Console.Write($"ERROR: Invalid wire color, {wires[i]} is not a valid color. Enter [C] to continue or [X] To Quit. ");
                            string cont = Console.ReadLine().ToLower();
                            if (cont == "x") quit = true;
                            continue;
                    }
                }

                break;
            }
            #endregion

            #region Solve Wires
            // Check if module was quit
            if ( !quit )
            {
                switch (wires.Count)
                {
                    case 3: // Solve for 3 wires
                        if (!colors.Contains(Color.Red))
                            Console.WriteLine("Cut Second Wire");
                        else if (colors[colors.Count() - 1] == Color.White)
                            Console.WriteLine("Cut Last Wire");
                        else if (colors.IndexOf(Color.Blue) != colors.LastIndexOf(Color.Blue))
                            Console.WriteLine("Cut Last Blue Wire");
                        else
                            Console.WriteLine("Cut Last Wire");
                        break;

                    case 4: // Solve for 4 wires
                        if (colors.IndexOf(Color.Red) != colors.LastIndexOf(Color.Red) && lastSerial % 2 != 0)
                            Console.WriteLine("Cut Last Wire");
                        else if (colors.Last() == Color.Yellow && !colors.Contains(Color.Red))
                            Console.WriteLine("Cut First Wire");
                        else if (colors.Contains(Color.Blue) && colors.IndexOf(Color.Blue) == colors.LastIndexOf(Color.Blue))
                            Console.WriteLine("Cut First Wire");
                        else if (colors.IndexOf(Color.Yellow) != colors.LastIndexOf(Color.Yellow))
                            Console.WriteLine("Cut Last Wire");
                        else
                            Console.WriteLine("Cut Second Wire");
                        break;

                    case 5: // Solve for 5 wires
                        if (colors[colors.Count() - 1] == Color.Black && lastSerial % 2 != 0)
                            Console.WriteLine("Cut Fourth Wire");
                        else if (colors.Contains(Color.Red) && colors.IndexOf(Color.Red) == colors.LastIndexOf(Color.Red)
                            && colors.IndexOf(Color.Yellow) != colors.LastIndexOf(Color.Yellow))
                            Console.WriteLine("Cut First Wire");
                        else if (!colors.Contains(Color.Black))
                            Console.WriteLine("Cut Second Wire");
                        else
                            Console.WriteLine("Cut First Wire");
                        break;

                    case 6: // Solve for 6 wires
                        if (!colors.Contains(Color.Yellow) && lastSerial % 2 != 0)
                            Console.WriteLine("Cut Third Wire");
                        else if (colors.Contains(Color.Yellow) && colors.IndexOf(Color.Yellow) == colors.LastIndexOf(Color.Yellow)
                            && colors.IndexOf(Color.White) != colors.LastIndexOf(Color.White))
                            Console.WriteLine("Cut Fourth Wire");
                        else if (!colors.Contains(Color.Red))
                            Console.WriteLine("Cut Last Wire");
                        else
                            Console.WriteLine("Cut Fourth Wire");
                        break;
                }
            }
            #endregion
        }

        /// <summary>
        /// Solve "Button" Module
        /// </summary>
        /// <param name="numBatt">number of batteries</param>
        public void Button(ref int numBatt)
        {
            Color color = Color.Null;
            string word = "";
            bool quit = false;

            // Check Batteries
            if (numBatt < 0)
            {
                Console.Write("\nEnter # of Batteries: ");
                numBatt = int.Parse(Console.ReadLine());
            }

            #region Input Button
            while (!quit)
            {
                // Get button color
                Console.WriteLine("\nColors: r (red) | y (yellow | b (blue) | bl (black | w (white) ");
                Console.Write("Enter Button Color: ");
                string buttonColor = Console.ReadLine().ToLower();

                // Get button word
                Console.Write("Enter Button Word: ");
                word = Console.ReadLine().ToLower();

                // Check color and word
                if (buttonColor != "r" && buttonColor != "y" && buttonColor != "b" &&
                        buttonColor != "bl" && buttonColor != "w")
                {
                    Console.Write($"ERROR: Invalid button color, {buttonColor} is not a valid color. Enter [C] to continue or [X] To Quit. ");
                    string cont = Console.ReadLine().ToLower();
                    if (cont == "x") quit = true;
                    continue;
                }

                if (word != "abort" && word != "detonate" && 
                    word != "hold" && word != "press")
                {
                    Console.Write($"ERROR: Invalid word, {word} is not a valid word. Enter [C] to continue or [X] To Quit. ");
                    string cont = Console.ReadLine().ToLower();
                    if (cont == "x") quit = true;
                    continue;
                }

                // Swap color to enum
                switch (buttonColor)
                {
                    case "r": color = Color.Red; break;
                    case "y": color = Color.Yellow; break;
                    case "b": color = Color.Blue; break;
                    case "bl": color = Color.Black; break;
                    case "w": color = Color.White; break;
                }

                break;
            }
            #endregion

            #region Solve Button
            if (!quit)
            {
                if (color == Color.Blue && word == "abort")
                {
                    Console.WriteLine("Hold and Release Based on Color. Blue = 4 | Yellow = 5 | Other = 1");
                    return;
                }
                if (numBatt > 1 && word == "detonate")
                {
                    Console.WriteLine("Press and Release");
                    return;
                } 
                if (color == Color.White)
                {
                    //Check for CAR indicator
                    Console.Write("Is there a lit CAR indicator (Y/N): ");
                    string ans = Console.ReadLine().ToLower();
                    bool carInd = ans == "y";

                    if (carInd)
                    {
                        Console.WriteLine("Hold and Release Based on Color. Blue = 4 | Yellow = 5 | Other = 1");
                        return;
                    } 
                }
                if (numBatt > 2)
                {
                    //Check for FRK indicator
                    Console.Write("Is there a lit FRK indicator (Y/N): ");
                    string ans = Console.ReadLine().ToLower();
                    bool frkInd = ans == "y";

                    if (frkInd)
                    {
                        Console.WriteLine("Press and Release");
                        return;
                    }
                }
                if (color == Color.Yellow)
                {
                    Console.WriteLine("Hold and Release Based on Color. Blue = 4 | Yellow = 5 | Other = 1");
                    return;
                }
                if (color == Color.Red && word == "hold")
                {
                    Console.WriteLine("Press and Release");
                    return;
                }
                Console.WriteLine("Hold and Release Based on Color. Blue = 4 | Yellow = 5 | Other = 1");
            }
            #endregion
        }

        /// <summary>
        /// Solve the "Keypad" Module
        /// </summary>
        public void Keypad()
        {
            // Setup the six sollution lists
            List<Symbol> columb1 = new List<Symbol>() { Symbol.Balloon, Symbol.AT, Symbol.UpsideDownY, Symbol.SquigglyN, Symbol.SquidKnife, Symbol.HookN, Symbol.LeftC };
            List<Symbol> columb2 = new List<Symbol>() { Symbol.Euro, Symbol.Balloon, Symbol.LeftC, Symbol.Cursive, Symbol.HollowStar, Symbol.SquigglyN, Symbol.QuestionMark };
            List<Symbol> columb3 = new List<Symbol>() { Symbol.Copyright, Symbol.Pumpkin, Symbol.Cursive, Symbol.DoubleK, Symbol.MeltedThree, Symbol.UpsideDownY, Symbol.HollowStar };
            List<Symbol> columb4 = new List<Symbol>() { Symbol.Six, Symbol.Paragraph, Symbol.BT, Symbol.SquidKnife, Symbol.DoubleK, Symbol.QuestionMark, Symbol.SmileyFace };
            List<Symbol> columb5 = new List<Symbol>() { Symbol.Pitchfork, Symbol.SmileyFace, Symbol.BT, Symbol.RightC, Symbol.Paragraph, Symbol.Dragon, Symbol.FilledStar };
            List<Symbol> columb6 = new List<Symbol>() { Symbol.Six, Symbol.Euro, Symbol.Tracks, Symbol.AE, Symbol.Pitchfork, Symbol.NWithHat, Symbol.Omega };
            List<List<Symbol>> solutions = new List<List<Symbol>>() { columb1, columb2, columb3, columb4, columb5, columb6 } ;

            
            List<string> symbolsString = new List<string>();
            List<Symbol> userSymbols = new List<Symbol>();
            int solutionCol = int.MinValue;

            while (true)
            {
                #region Let user input their symbols
                Console.WriteLine("\nSymbols: Copyright | FilledStar | HollowStar | SmileyFace | " +
                                "DoubleK | Omega | SquidKnife | Pumpkin | HookN | Six | SquigglyN | " +
                                "AT | AE | MeltedThree | Euro | NWithHat | Dragon | QuestionMark | " +
                                "Paragraph | RightC | LeftC | Pitchfork | Cursive | Tracks | " +
                                "Balloon | UpsideDownY | BT");
                Console.Write("Enter your 4 symbols: ");
                string input = Console.ReadLine().ToLower();

                // Split wires into list
                symbolsString.Clear();
                symbolsString.AddRange(input.Split(' '));

                // Check for correct number of symbols
                if (symbolsString.Count != 4)
                {
                    Console.Write("ERROR: Invalid number of symbols, enter 4 symbols. Enter [C] to continue or [X] To Quit. ");
                    string cont = Console.ReadLine().ToLower();
                    if (cont == "x") return;
                    continue;
                }

                // change list into enums
                userSymbols.Clear();
                foreach (string symbol in symbolsString)
                {
                    switch(symbol)
                    {
                        case "copyright": userSymbols.Add(Symbol.Copyright); break;
                        case "filledstar": userSymbols.Add(Symbol.FilledStar); break;
                        case "hollowstar": userSymbols.Add(Symbol.HollowStar); break;
                        case "smileyface": userSymbols.Add(Symbol.SmileyFace); break;
                        case "doublek": userSymbols.Add(Symbol.DoubleK); break;
                        case "omega": userSymbols.Add(Symbol.Omega); break;
                        case "squidknife": userSymbols.Add(Symbol.SquidKnife); break;
                        case "pumpkin": userSymbols.Add(Symbol.Pumpkin); break;
                        case "hookn": userSymbols.Add(Symbol.HookN); break;
                        case "six": userSymbols.Add(Symbol.Six); break;
                        case "squigglyn": userSymbols.Add(Symbol.SquigglyN); break;
                        case "at": userSymbols.Add(Symbol.AT); break;
                        case "ae": userSymbols.Add(Symbol.AE); break;
                        case "meltedthree": userSymbols.Add(Symbol.MeltedThree); break;
                        case "euro": userSymbols.Add(Symbol.Euro); break;
                        case "nwithhat": userSymbols.Add(Symbol.NWithHat); break;
                        case "dragon": userSymbols.Add(Symbol.Dragon); break;
                        case "questionmark": userSymbols.Add(Symbol.QuestionMark); break;
                        case "paragraph": userSymbols.Add(Symbol.Paragraph); break;
                        case "rightc": userSymbols.Add(Symbol.RightC); break;
                        case "leftc": userSymbols.Add(Symbol.LeftC); break;
                        case "pitchfork": userSymbols.Add(Symbol.Pitchfork); break;
                        case "cursive": userSymbols.Add(Symbol.Cursive); break;
                        case "tracks": userSymbols.Add(Symbol.Tracks); break;
                        case "balloon": userSymbols.Add(Symbol.Balloon); break;
                        case "upsidedowny": userSymbols.Add(Symbol.UpsideDownY); break;
                        case "bt": userSymbols.Add(Symbol.BT); break;

                        default:
                            Console.WriteLine($"ERROR: Invalid symbol, {symbol} is not a valid symbol. Enter [C] to continue or [X] To Quit. ");
                            string cont = Console.ReadLine().ToLower();
                            if (cont == "x") return;
                            continue;
                    }
                }
                #endregion

                // Figure out which list contains all four symbols
                
                for (int i = 0; i < 6; i++)
                {
                    // check if solution columb contains all 4 user symbols
                    if (solutions[i].Contains(userSymbols[0]) && solutions[i].Contains(userSymbols[1]) && solutions[i].Contains(userSymbols[2]) && solutions[i].Contains(userSymbols[3]))
                    {
                        solutionCol = i;
                        break;
                    }
                }

                // check that a solution columb was found
                if (solutionCol == int.MinValue)
                {
                    Console.WriteLine("ERROR: Solution does not exist, please double check your symbols and try again. Enter [C] to continue or [X] To Quit. ");
                    string cont = Console.ReadLine().ToLower();
                    if (cont == "x") return;
                    continue;
                }

                break;
            }

            
            // Figure out the order of the symbols
            List<Symbol> solutionOrder = new List<Symbol>();
            foreach (Symbol sym in solutions[solutionCol])
            {
                if (userSymbols.Contains(sym))
                {
                    solutionOrder.Add(sym);
                }
            }

            // Send order of symbols to solve the module
            Console.WriteLine($"The Solution is: {solutionOrder[0]}, {solutionOrder[1]}, {solutionOrder[2]}, {solutionOrder[3]}");
        }

        /// <summary>
        /// Solve "Simon Says" Module
        /// </summary>
        /// <param name="hasVowel">Does the serial number contain a vowel</param>
        /// <param name="numStrikes">Number of strikes on the bomb</param>
        public void SimonSays(ref bool hasVowel, ref int numStrikes)
        {
            #region Set Solution Dictionary
            // Setup possible solution dictionarys
            Dictionary<Color, Color> vowel0Strikes = new Dictionary<Color, Color>() { { Color.Red, Color.Blue }, {Color.Blue, Color.Red }, {Color.Green, Color.Yellow }, { Color.Yellow, Color.Green } };
            Dictionary<Color, Color> vowel1Strikes = new Dictionary<Color, Color>() { { Color.Red, Color.Yellow }, { Color.Blue, Color.Green }, { Color.Green, Color.Blue }, { Color.Yellow, Color.Red } };
            Dictionary<Color, Color> vowel2Strikes = new Dictionary<Color, Color>() { { Color.Red, Color.Green }, { Color.Blue, Color.Red }, { Color.Green, Color.Yellow }, { Color.Yellow, Color.Blue } };
            Dictionary<Color, Color> noVowel0Strikes = new Dictionary<Color, Color>() { { Color.Red, Color.Blue }, { Color.Blue, Color.Yellow }, { Color.Green, Color.Green }, { Color.Yellow, Color.Red } };
            Dictionary<Color, Color> noVowel1Strikes = new Dictionary<Color, Color>() { { Color.Red, Color.Red }, {Color.Blue, Color.Blue }, {Color.Green, Color.Yellow }, { Color.Yellow, Color.Green } };
            Dictionary<Color, Color> noVowel2Strikes = new Dictionary<Color, Color>() { { Color.Red, Color.Yellow }, {Color.Blue, Color.Green }, {Color.Green, Color.Blue }, { Color.Yellow, Color.Red } };
            Dictionary<Color, Color> solutionDict = new Dictionary<Color, Color>();

            // Set correct solution dictionary based on serial number and number of strikes
            if (hasVowel)
            {
                switch (numStrikes)
                {
                    case 0: solutionDict = vowel0Strikes; break;
                    case 1: solutionDict = vowel1Strikes; break;
                    case 2: solutionDict = vowel2Strikes; break;
                }
            }
            else
            {
                switch (numStrikes)
                {
                    case 0: solutionDict = noVowel0Strikes; break;
                    case 1: solutionDict = noVowel1Strikes; break;
                    case 2: solutionDict = noVowel2Strikes; break;
                }
            }
            #endregion

            // Loop until Simon is solved
            bool isSolved = false;
            List<Color> sequence = new List<Color>();
            while (!isSolved)
            {
                // Have user give the next color in sequence
                Console.WriteLine("\nColors: b (blue) | r (red) | y (yellow) | g (green)");
                Console.Write("Enter the last color to be shown. Or if the module is disarmed enter d (done/disarmed): ");
                string input = Console.ReadLine().ToLower().Trim();

                // Add input color to sequence list
                switch (input)
                {
                    case "b": sequence.Add(Color.Blue); break;
                    case "r": sequence.Add(Color.Red); break;
                    case "y": sequence.Add(Color.Yellow); break;
                    case "g": sequence.Add(Color.Green); break;
                    case "d": isSolved = true; continue;

                    default:
                        Console.WriteLine("ERROR: Invalid color input pleas try again");
                        continue;
                }

                // Output solution to current step of simon
                Console.Write("Step Solution: ");
                foreach (Color c in sequence)
                {
                    Console.Write($"{solutionDict[c]}, ");
                }
                Console.WriteLine();
            }
        }

        /// <summary>
        /// Solve the "Who's on First" Module
        /// </summary>
        public void WhosOnFirst()
        {
            // Trackers
            bool located = false;
            bool decrypted = false;
            int stage = 1;

            while (stage <= 3)
            {
                Console.WriteLine();

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
                        Console.Write("ERROR: Invalid Word, Try Again. Enter [C] to continue or [X] To Quit. ");
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
                    switch (decrypt)
                    {
                        case "blank":
                            Console.WriteLine("WAIT, RIGHT, OKAY, MIDDLE, BLANK");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "done":
                            Console.WriteLine("SURE, UH HUH, NEXT, WHAT? YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, YOU ARE, UH UH, DONE");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "first":
                            Console.WriteLine("LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, BLANK, WHAT, PRESS, FIRST");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "hold":
                            Console.WriteLine("YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "left":
                            Console.WriteLine("RIGHT, LEFT");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "like":
                            Console.WriteLine("YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "middle":
                            Console.WriteLine("BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, MIDDLE");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "next":
                            Console.WriteLine("WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "no":
                            Console.WriteLine("BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, PRESS, OKAY, NO");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "nothing":
                            Console.WriteLine("UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, WAIT, FIRST, NOTHING");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "okay":
                            Console.WriteLine("MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "press":
                            Console.WriteLine("RIGHT, MIDDLE, YES, READY, PRESS");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "ready":
                            Console.WriteLine("YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "right":
                            Console.WriteLine("YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "sure":
                            Console.WriteLine("YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "u":
                            Console.WriteLine("UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "uh huh":
                            Console.WriteLine("UH HUH");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "uh uh":
                            Console.WriteLine("UR, U, YOU ARE, YOU'RE, NEXT, UH UH");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "uhhh":
                            Console.WriteLine("READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, UHHH");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "ur":
                            Console.WriteLine("DONE, U, UR");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "wait":
                            Console.WriteLine("UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "what":
                            Console.WriteLine("UHHH, WHAT");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "what?":
                            Console.WriteLine("YOU, HOLD, YOU'RE. YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, UR, NEXT, WHAT?");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "yes":
                            Console.WriteLine("OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "you":
                            Console.WriteLine("SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "you are":
                            Console.WriteLine("YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, YOU'RE, SURE, UR, YOU ARE");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "you're":
                            Console.WriteLine("YOU, YOU'RE");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        case "your":
                            Console.WriteLine("UH UH, YOU ARE, UH HUH, YOUR");
                            decrypted = true;
                            stage += 1;
                            located = false;
                            break;

                        default:
                            Console.Write("ERROR: Invalid Word, Try Again. Enter [C] to continue or [X] To Quit. ");
                            string cont = Console.ReadLine().ToLower();

                            if (cont == "x")
                            {
                                located = true;
                                decrypted = true;
                                stage = 4;
                            }
                            break;
                    }
                }
                #endregion
            }
        }
    }
}