# =====================================================================
# 1. CONFIGURATION & DATA LAYER
# =====================================================================

def get_knowledge_base():
    return {
        ("hello", "hi", "hey"): "Hi there! Welcome to the YHM Logic Engine. How can I help you today?",
        ("logic", "architecture", "whitebox"): "We use a 'white box' architecture here: Input -> Sanitization -> Hash Map Lookup -> Output. [cite: 58, 75]",
        ("status", "operation", "health"): "System operation: 100% deterministic. Zero hallucination risk detected. [cite: 34, 59]",
        ("ai", "intelligence", "deeplearning"): "Artificial Intelligence is about building intelligent systems. Today, we master deterministic logic before moving to deep learning. [cite: 8, 9]",
        ("chatbot", "bot", "interface"): "This is a rule-based AI chatbot acting as a deterministic filter or control layer to simulate human interaction. [cite: 7, 10, 71]",
        ("automation", "workflow", "compliance"): "Automation replaces manual tasks with rule-based workflows, ensuring high compliance and safety in data flow. [cite: 60, 73]",
        ("bye", "goodbye", "quit"): "Goodbye! Keep mastering the logic engine. [cite: 53]"
    }

# =====================================================================
# 2. INPUT PROCESSING & SANITIZATION
# =====================================================================

def sanitize_input(raw_text: str) -> str:
    return raw_text.lower().strip() # [cite: 110, 207]

# =====================================================================
# 3. INTERFACE HELPER & UTILITIES
# =====================================================================

def display_help_menu(knowledge_base):
    print("\n" + "-" * 50)
    print("📋 AVAILABLE COMMANDS & TOPICS")
    print("-" * 50)
    print("You can type full sentences or just the keywords below:")
    print("  • 'hello' or 'hi'         -> Say hello to the system")
    print("  • 'ai' or 'intelligence'  -> Learn about the AI philosophy")
    print("  • 'chatbot' or 'bot'      -> Learn about this interface architecture")
    print("  • 'automation'            -> Read about rule-based workflows")
    print("  • 'logic' or 'whitebox'   -> View the data flow structure")
    print("  • 'status' or 'health'    -> Check the system execution metrics")
    print("  • 'exit' or 'quit'        -> Safely close the application loop")
    print("-" * 50)

# =====================================================================
# 4. INTENT EVALUATION ENGINE
# =====================================================================

def match_intent(clean_input: str, knowledge_base: dict) -> str:
    for keywords, response in knowledge_base.items():
        if clean_input in keywords:
            return response # [cite: 154, 207]
            
    for keywords, response in knowledge_base.items():
        for keyword in keywords:
            if keyword in clean_input:
                return response
                
    return None

# =====================================================================
# 5. CORE HEARTBEAT & CONTROL LAYER LOOP
# =====================================================================

def run_chatbot_cli():
    knowledge_base = get_knowledge_base()
    
    print("=" * 65)
    print("          🤖 YHM LOGIC ENGINE v2.5 — PRODUCTION CLI 🤖")
    print("=" * 65)
    print("  System Status: ONLINE")
    print("  Instructions : Type your question naturally below.")
    print("                 Type 'help' to see the command dashboard.")
    print("                 Type 'exit' to turn off the engine safely.")
    print("=" * 65)
    
    # Initial bot greeting message displayed right at startup
    print("\nBot: System initialized. Enter an intent to evaluate programmatic decision-making.") # [cite: 10]
    
    # 1. Continuous Loop Heartbeat [cite: 26, 114, 207]
    while True:
        try:
            raw_input = input("\nYou: ") # [cite: 110]
        except (KeyboardInterrupt, EOFError):
            print("\n\nBot: Force termination signal received. Exiting safely...")
            break
            
        # 2. Input Sanitization Phase [cite: 80, 207]
        clean_input = sanitize_input(raw_input)
        
        if not clean_input:
            continue
            
        # 3. Intercept Exit Strategy [cite: 23, 121, 208]
        if clean_input in ('exit', 'quit', 'terminate', 'kill'):
            print("\nBot: Terminating control loop. Milestone verified. Goodbye! [cite: 15, 121]")
            print("=" * 65 + "\n")
            break
            
        if clean_input in ('help', 'commands', 'menu', '?'):
            display_help_menu(knowledge_base)
            continue
            
        # 4. Intent Evaluation via Hash Map Structure [cite: 154, 207]
        reply = match_intent(clean_input, knowledge_base)
        
        # 5. Response Generation [cite: 58, 89, 94]
        if reply:
            print(f"Bot: {reply}")
        else:
            print("Bot: I couldn't find a direct keyword match in my logic engine. [cite: 208]")
            print("     Type 'help' to view the full command dashboard of valid topics. [cite: 208]")

# =====================================================================
# 6. APPLICATION ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    run_chatbot_cli()