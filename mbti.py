import numpy as np
from difflib import SequenceMatcher
            
class MBTI_Personality:
    def __init__(self):
        self.questions = None
        self.answers = np.zeros(50)  # Initialize with zeros for up to 50 questions
        self.types = None
        self.functions = np.array(["Ni", "Ne", "Si", "Se", "Ti", "Te", "Fi", "Fe"])
        self.sums = np.zeros(8)
        self.functionStr = ""
        self.personalityTypes = None
        self.personalityStacks = None
        
    def initializeQuestions(self):
        self.questions = np.array([
            "I feel energized when I spend time with a lot of people.",
            "I focus on details and specifics when learning something new.",
            "I prioritize logic and objectivity when making decisions.",
            "I prefer to have a plan and stick to it.",
            "I find it easy to relate to people and understand their perspective.",
            "I prefer to reflect quietly by myself.",
            "I enjoy thinking about the future and the possibilities it holds.",
            "I consider people's feelings when making decisions.",
            "I am comfortable with changes and surprises.",
            "I enjoy solving complex problems and puzzles.",
            "I enjoy being the center of attention.",
            "I rely on my experiences when making decisions.",
            "I am straightforward and direct in my communication.",
            "I like to complete tasks well before the deadline.",
            "I prefer to focus on one task at a time.",
            "I often think before I speak.",
            "I trust my gut feelings and intuition.",
            "I try to be tactful and considerate in my communication.",
            "I often leave tasks until the last minute.",
            "I often find myself multi-tasking.",
            "I seek out social events and gatherings.",
            "I prefer clear and concrete information over abstract ideas.",
            "I value fairness and justice.",
            "I prefer structured environments with clear rules.",
            "I am drawn to artistic and creative activities.",
            "I need time alone to recharge after social interactions.",
            "I enjoy brainstorming and considering various ideas.",
            "I value empathy and compassion.",
            "I enjoy flexibility and spontaneity.",
            "I like to gather facts and data before making decisions.",
            "I like to talk through my problems.",
            "I am practical and down-to-earth.",
            "I enjoy analyzing problems and finding logical solutions.",
            "I like to keep my space organized and tidy.",
            "I like to think big picture rather than the details.",
            "I tend to keep my thoughts and feelings to myself.",
            "I often get lost in my own imagination.",
            "I am concerned with maintaining harmony in my relationships.",
            "I am adaptable and go with the flow.",
            "I am thorough and detail-oriented in my work.",
            "I prefer to work in teams rather than alone.",
            "I like to focus on what is happening right now.",
            "I am more likely to criticize than to compliment.",
            "I set goals and work systematically towards them.",
            "I prefer practical and hands-on activities.",
            "I enjoy deep, one-on-one conversations.",
            "I am drawn to concepts and theories.",
            "I often find myself putting others' needs ahead of my own.",
            "I prefer to keep my options open.",
            "I often contemplate the meaning and purpose of life."
        ])
        self.types = np.array([
            "E", "S", "T", "J", "F", "I", "N", "F", "P", "T", "E", "S", "T", "J", "S",
            "I", "N", "F", "P", "N", "E", "S", "T", "J", "N", "I", "N", "F", "P", "S",
            "E", "S", "T", "J", "P", "I", "N", "F", "P", "S", "E", "S", "T", "J", "P",
            "I", "N", "F", "P", "N"
        ])
        
    def initializePersonalities(self):
        self.personalityTypes = np.array(["ESFJ", "ISFJ", "ESTJ", "ISTJ", "ENFJ", "INFJ", "ENFP", "INFP", "ESFP", "ISFP", "ESTP", "ISTP", "ENTJ", "INTJ", "ENTP", "INTP"])
        self.personalityStacks = np.array(["Fe-Si-Ne-Ti", "Si-Fe-Ti-Ne", "Te-Si-Ne-Fi", "Si-Te-Fi-Ne", "Fe-Ni-Se-Ti", "Ni-Fe-Ti-Se", "Ne-Fi-Te-Si", "Se-Fi-Te-Ni", "Fi-Se-Ni-Te", "Se-Ti-Fe-Ni", "Ti-Se-Ni-Fe", "Te-Ni-Se-Fi", "Ni-Te-Fi-Se", "Ne-Ti-Fe-Si", "Ti-Ne-Si-Fe"])
        
    def takingTest(self):
        self.initializeQuestions()
        self.initializePersonalities()
        
        print("\n------- MBTI Personality Test -------")
        print("Let us commence...")
        print("**Please answer all questions in a range of 1-7 and type 'BREAK' to leave at any time**")
        print("However, for best results, it is recommended to answer all 50 questions.")
        Qnumber = 1
        answers = []
        for question in self.questions:
            inputted_answer = input(f"{Qnumber}. {question} ")
            if inputted_answer.upper() == "BREAK":
                break
            try:
                inputted_answer = int(inputted_answer)
            except ValueError:
                print("Invalid input, please enter a number between 1 and 7 or 'BREAK'.")
                continue
            
            while inputted_answer < 1 or inputted_answer > 7:
                print("Answer out of range - please re-enter!")
                inputted_answer = input(f"{Qnumber}. {question} ")
                if inputted_answer.upper() == "BREAK":
                    break
                try:
                    inputted_answer = int(inputted_answer)
                except ValueError:
                    print("Invalid input, please enter a number between 1 and 7 or 'BREAK'.")
                    continue
            
            if isinstance(inputted_answer, int):
                answers.append(inputted_answer)
                Qnumber += 1
        
        self.answers[:len(answers)] = answers
        
        self.sums[0] = self.answers[self.types == "I"].sum() + self.answers[self.types == "N"].sum()
        self.sums[1] = self.answers[self.types == "E"].sum() + self.answers[self.types == "N"].sum()
        self.sums[2] = self.answers[self.types == "I"].sum() + self.answers[self.types == "S"].sum()
        self.sums[3] = self.answers[self.types == "E"].sum() + self.answers[self.types == "S"].sum()
        self.sums[4] = self.answers[self.types == "I"].sum() + self.answers[self.types == "T"].sum()
        self.sums[5] = self.answers[self.types == "E"].sum() + self.answers[self.types == "T"].sum()
        self.sums[6] = self.answers[self.types == "I"].sum() + self.answers[self.types == "F"].sum()
        self.sums[7] = self.answers[self.types == "E"].sum() + self.answers[self.types == "F"].sum()     
        print("TEST COMPLETE.")
        
        self.analyzeResults()
        
    def analyzeResults(self):
        sorted_indices = np.argsort(self.sums)[::-1]
        sorted_functions = self.functions[sorted_indices]
        sorted_sums = self.sums[sorted_indices]
        
        print(" ")
        
        for func, s in zip(sorted_functions, sorted_sums):
            print(f"{func}: {s}")
            
        self.functionStr = "-".join(sorted_functions[:4])
        print("Your final function stack is..." + self.functionStr)
        
        self.findClosestMatches()
        
        print("\n**This test is purely for fun and to learn more about yourself, so do not take the results too strongly.**")
        print(" ")
        
    def findClosestMatches(self):
        if self.functionStr == "":
            print("Function string is empty. Please analyze results first.")
            return
        
        similarities = np.array([SequenceMatcher(None, self.functionStr, stack).ratio() for stack in self.personalityStacks])
        sorted_indices = np.argsort(similarities)[::-1]
        
        top_three_indices = sorted_indices[:3]
        top_three_personalities = self.personalityTypes[top_three_indices]
        top_three_similarities = similarities[top_three_indices]
        
        print("\nTop 3 closest matches:")
        for i in range(3):
            print(f"{top_three_personalities[i]}: {top_three_similarities[i]:.2f}")
