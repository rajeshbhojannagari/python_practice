count=0
answers=[]
Questions=["Who developed Python Programming Language?",
           "Which type of Programming does Python support?",
           "Is Python case sensitive when dealing with identifiers?",
           "Which of the following is the correct extension of the Python file?",
           "Is Python code compiled or interpreted?",
           "All keywords in Python are in",
           "Which of the following is used to define a block of code in Python language?",
           "Which keyword is used for function in Python language?",
           "Which of the following character is used to give single-line comments in Python?",
           "Python supports the creation of anonymous functions at runtime, using a construct called"]
Options=[["Wick van Rossum","Rasmus Lerdorf","Guido van Rossum","Niene Stom"],
         ["object-oriented programming","structured programming","functional programming","all of the mentioned"],
         ["no","yes","machine dependent","none of the mentioned"],
         [".python",".pl",".py",".p"],
         ["Python code is both compiled and interpreted","Python code is neither compiled nor interpreted","Python code is only compiled","Python code is only interpreted"],
         ["Capitalized","lower case","UPPER CASE","None of the mentioned"],
         ["Indentation","Key","Brackets"," All of the mentioned"],
         ["Function","def","Fun","Define"],
         ["//","#","!"," /*"],
         ["pi","anonymous","lambda","none of the mentioned"]]
Correct=['c','d','b','c','a','d','a','b','b','c']
for i in range(len(Questions)):
    print(i+1,Questions[i])
    print("a.",Options[i][0])
    print("b.",Options[i][1])
    print("c.",Options[i][2])
    print("d.",Options[i][3])
    while True:
        TypeAns=input("Enter a or b or c or d: ").lower()
        if TypeAns in['a','b','c','d']:
            answers.append(TypeAns)
            break
        else:
            print("Invalid Key")   
for a in range(len(Correct)):
    if (answers[a]==Correct[a]):
        count=count+1
print("Your Marks are ",count)
    
