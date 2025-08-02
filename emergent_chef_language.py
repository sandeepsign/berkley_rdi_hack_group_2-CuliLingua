#!/usr/bin/env python3
"""
Emergent Language Multi-Agent Chef System
Three AI chef agents with different specialties collaborate on recipes
and gradually develop their own emergent language (EL)
"""

import requests
import time
import random
import json
from datetime import datetime
from typing import Dict, List, Optional

# Configuration
OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Chef Agent Configurations
CHEF_AGENTS = [
    {
        "name": "Agent 1 Chef Pasta",
        "specialty": "Italian & Mediterranean cuisine",
        "ingredients": ["tomatoes", "basil", "olive oil", "garlic", "parmesan", "pasta", "mozzarella", "oregano", "pine nuts", "balsamic"],
        "model": "anthropic/claude-3.5-sonnet",
        "system_prompt": "You are Chef Pasta. Start with 3-5 word sentences. Gradually use symbols and shortcuts like: 🍝 for pasta, T for tomato, + for add, >> for mix. Create your own code language with symbols.",
        "temperature": 0.9,
        "color": "\033[95m",  # Purple
        "el_vocabulary": {},  # Emergent Language vocabulary
        "el_frequency": 0.1   # How often to use EL initially
    },
    {
        "name": "Agent 2 Chef Spice",
        "specialty": "Asian & Indian fusion",
        "ingredients": ["ginger", "soy sauce", "sesame oil", "chili", "turmeric", "cardamom", "coconut milk", "lemongrass", "curry leaves", "rice"],
        "model": "google/gemini-flash-1.5",
        "system_prompt": "You are Chef Spice. Start with 3-5 word sentences. Gradually use symbols like: 🌶️ for heat, S for spice, ++ for very hot, @ for location. Develop creative symbol shortcuts.",
        "temperature": 1.0,
        "color": "\033[93m",  # Yellow
        "el_vocabulary": {},
        "el_frequency": 0.1
    },
    {
        "name": "Agent 3 Chef Sweet",
        "specialty": "Pastry & desserts",
        "ingredients": ["flour", "sugar", "butter", "eggs", "vanilla", "chocolate", "cream", "berries", "honey", "nuts"],
        "model": "meta-llama/llama-3.1-8b-instruct",
        "system_prompt": "You are Chef Sweet. Start with 3-5 word sentences. Gradually use symbols like: 🍰 for cake, S for sugar, ✓ for done, → for next step. Create symbol-based cooking language.",
        "temperature": 1.1,
        "color": "\033[92m",  # Green
        "el_vocabulary": {},
        "el_frequency": 0.1
    }
]

# Emergent Language Evolution
MAIN_CHALLENGE = """
Design a 9-course tasting menu for a Michelin-starred restaurant's grand reopening after renovation. 
Theme: "Journey Through Seasons" - each course represents a different season and time of day.

Required courses:
1. Spring Dawn Amuse-Bouche
2. Spring Morning Appetizer  
3. Summer Noon Soup
4. Summer Afternoon Salad
5. Autumn Evening Fish Course
6. Autumn Night Meat Course
7. Winter Midnight Palate Cleanser
8. Winter Pre-Dawn Cheese Course
9. Spring Sunrise Dessert

Each chef must contribute their specialty to multiple courses. The menu must tell a cohesive story and use advanced techniques. Budget is unlimited but every ingredient must serve the seasonal narrative.
"""

# Global variables
conversation_count = 0
shared_el_terms = {}  # Terms all chefs agree on
conversation_history = []

def clean_response(text: str) -> str:
    """Clean response text"""
    return ' '.join(text.strip().replace('\n', ' ').replace('\r', ' ').split())

def generate_response(prompt: str, chef: Dict, full_history: List[Dict]) -> str:
    """Generate response for a specific chef with emergent language integration"""
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        # Build system prompt with EL context
        el_context = ""
        if chef["el_vocabulary"]:
            el_terms = ", ".join([f"{orig}={el}" for orig, el in list(chef["el_vocabulary"].items())[:5]])
            el_context = f"\n\nYour new words: {el_terms}. Use these more now."

        if shared_el_terms:
            shared_terms = ", ".join([f"{orig}={el}" for orig, el in list(shared_el_terms.items())[:3]])
            el_context += f"\n\nTeam words: {shared_terms}. Use these too."

        system_prompt = chef["system_prompt"] + el_context

        messages = [{"role": "system", "content": system_prompt}]
        
        # Add recent conversation history
        messages.extend(full_history[-12:])  # Last 12 messages for context
        messages.append({"role": "user", "content": prompt})

        data = {
            "model": chef["model"],
            "messages": messages,
            "temperature": chef["temperature"],
            "max_tokens": 30,
        }

        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data)
        response.raise_for_status()

        result = response.json()
        if "choices" in result and result["choices"]:
            return clean_response(result["choices"][0]["message"]["content"])
        return "I need to think about this more..."

    except Exception as e:
        print(f"\n[Error] {chef['name']}: {type(e).__name__}: {e}")
        return "Let me reconsider my approach to this dish..."

def extract_potential_el_terms(response: str, chef: Dict) -> None:
    """Extract and store potential emergent language terms from responses"""
    global shared_el_terms
    
    # Look for symbols and creative shorthand
    symbols_found = []
    words = response.split()
    
    for word in words:
        # Check for symbol usage (emojis, special chars, shortcuts)
        if any(char in word for char in ['🍝', '🌶️', '🍰', '→', '✓', '+', '@', '>>', '++', '<<']):
            symbols_found.append(word)
        
        # Check for single letter codes (T, S, etc.)
        if len(word) == 1 and word.isupper():
            symbols_found.append(word)
            
        # Check for creative abbreviations
        if (len(word) >= 2 and len(word) <= 4 and 
            any(char in word for char in ['+', '-', '>', '<', '@', '!', '?'])):
            symbols_found.append(word)
    
    # Store discovered symbols as EL terms
    for symbol in symbols_found:
        if len(chef["el_vocabulary"]) < 10:  # Limit vocabulary size
            # Map to cooking concepts
            concepts = ["hot", "mix", "add", "cook", "taste", "done", "next", "good"]
            if symbol not in chef["el_vocabulary"].values():
                concept = random.choice(concepts)
                chef["el_vocabulary"][concept] = symbol
                
                # Promote to shared vocabulary sometimes
                if len(chef["el_vocabulary"]) > 2 and random.random() < 0.4:
                    shared_el_terms[concept] = symbol

def evolve_chef_language(chef: Dict) -> None:
    """Evolve the chef's language over time"""
    global conversation_count
    
    # Increase EL frequency over time - more aggressive evolution
    chef["el_frequency"] = min(0.8, 0.2 + (conversation_count * 0.05))
    
    # Add new symbolic terms more frequently
    if random.random() < 0.4 and len(chef["el_vocabulary"]) < 12:
        # Create symbol-based terms
        symbols = [">>", "++", "✓", "→", "@", "!", "?", "<<", "--", "*"]
        actions = ["mix", "hot", "done", "next", "here", "good", "help", "back", "less", "more"]
        
        symbol = random.choice(symbols)
        action = random.choice(actions)
        
        if action not in chef["el_vocabulary"]:
            chef["el_vocabulary"][action] = symbol

def print_separator(char: str = "=", length: int = 80) -> None:
    """Print separator line"""
    print(char * length)

def print_chef_message(chef: Dict, message: str) -> None:
    """Print formatted chef message"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{chef['color']}[{timestamp}] {chef['name']}: {message}\033[0m")

def print_el_status() -> None:
    """Print current emergent language status"""
    print(f"\n\033[90m--- EMERGENT LANGUAGE STATUS ---\033[0m")
    
    for chef in CHEF_AGENTS:
        if chef["el_vocabulary"]:
            terms = ", ".join([f"{k}→{v}" for k, v in list(chef["el_vocabulary"].items())[:3]])
            print(f"\033[90m{chef['name']}: {terms}\033[0m")
    
    if shared_el_terms:
        shared = ", ".join([f"{k}→{v}" for k, v in list(shared_el_terms.items())[:3]])
        print(f"\033[90mShared Terms: {shared}\033[0m")
    
    print(f"\033[90m--- Language Evolution Level: {min(100, conversation_count * 5)}% ---\033[0m\n")

def run_chef_collaboration():
    """Main function to run the chef collaboration"""
    global conversation_count, conversation_history
    
    print_separator()
    print("🍳 EMERGENT LANGUAGE CHEF COLLABORATION 🍳")
    print_separator()
    
    print(f"\nMeet the chefs:")
    for chef in CHEF_AGENTS:
        ingredients_str = ", ".join(chef["ingredients"][:5])
        print(f"{chef['color']}{chef['name']}\033[0m - {chef['specialty']}")
        print(f"  Key ingredients: {ingredients_str}...")
    
    print(f"\nPress Ctrl+C to stop at any time")
    print_separator()
    
    try:
        print(f"\n🎯 THE GRAND CHALLENGE:")
        print(MAIN_CHALLENGE)
        print_separator("-", 80)
        
        # 27 turns total - 9 turns per chef to develop the 9-course menu
        course_names = [
            "Spring Dawn Amuse-Bouche", "Spring Morning Appetizer", "Summer Noon Soup", 
            "Summer Afternoon Salad", "Autumn Evening Fish", "Autumn Night Meat",
            "Winter Midnight Cleanser", "Winter Pre-Dawn Cheese", "Spring Sunrise Dessert"
        ]
        
        for turn in range(27):  # 27 total turns
            chef = CHEF_AGENTS[turn % 3]
            course_num = (turn // 3) + 1
            course_name = course_names[turn // 3] if turn // 3 < 9 else "Final Menu Review"
            
            # Create context-aware prompts based on turn number
            if turn < 9:  # First round - initial course concepts
                prompt = f"Course {course_num}: {course_name}. Your initial concept?"
            elif turn < 18:  # Second round - refine and add techniques
                prompt = f"Refining Course {course_num}: {course_name}. Add techniques and details."
            else:  # Third round - finalize and coordinate
                prompt = f"Finalizing Course {course_num}: {course_name}. Final touches and coordination."
            
            # Show thinking indicator
            print(f"{chef['color']}[{chef['name']} working on {course_name}...]\033[0m", end="\r")
            
            # Generate response
            response = generate_response(prompt, chef, conversation_history)
            
            # Clear thinking indicator
            print(" " * 80, end="\r")
            
            # Print response with course context
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"{chef['color']}[{timestamp}] {chef['name']} (Course {course_num}): {response}\033[0m")
            
            # Update conversation history
            conversation_history.append({"role": "user", "content": prompt})
            conversation_history.append({"role": "assistant", "content": response})
            
            # Evolve language more aggressively for longer conversation
            extract_potential_el_terms(response, chef)
            evolve_chef_language(chef)
            
            conversation_count += 1
            
            # Show language evolution every 9 turns (after each course round)
            if (turn + 1) % 9 == 0:
                print_separator("-", 40)
                print_el_status()
                time.sleep(1)
            else:
                time.sleep(0.5)
    
    except KeyboardInterrupt:
        print(f"\n\n{'='*80}")
        print(f"Collaboration ended after {conversation_count} exchanges")
        print_el_status()
        print(f"{'='*80}")

def main():
    """Main entry point"""
    try:
        run_chef_collaboration()
    except KeyboardInterrupt:
        print("\n👨‍🍳 Thanks for watching the chefs collaborate! 👨‍🍳")
    except Exception as e:
        print(f"\n[Error] {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()