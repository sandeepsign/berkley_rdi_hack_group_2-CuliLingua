# Emergent Language Chef Collaboration System

A multi-agent AI system where three specialized chef agents collaborate to design a 9-course Michelin-starred tasting menu while developing their own emergent symbolic language.

## 🍳 Overview

This system demonstrates emergent language development through specialized AI agents working together on complex culinary challenges. Three chef agents with different specialties gradually develop shared symbolic shortcuts and communication patterns as they collaborate.

## 👨‍🍳 The Agents

### Agent 1 Chef Pasta
- **Specialty**: Italian & Mediterranean cuisine
- **Key Ingredients**: tomatoes, basil, olive oil, garlic, parmesan, pasta, mozzarella, oregano, pine nuts, balsamic
- **Model**: Claude 3.5 Sonnet
- **Language Style**: Develops symbols like 🍝 for pasta, T for tomato, + for add, >> for mix

### Agent 2 Chef Spice  
- **Specialty**: Asian & Indian fusion
- **Key Ingredients**: ginger, soy sauce, sesame oil, chili, turmeric, cardamom, coconut milk, lemongrass, curry leaves, rice
- **Model**: Google Gemini Flash 1.5
- **Language Style**: Uses symbols like 🌶️ for heat, S for spice, ++ for very hot, @ for location

### Agent 3 Chef Sweet
- **Specialty**: Pastry & desserts
- **Key Ingredients**: flour, sugar, butter, eggs, vanilla, chocolate, cream, berries, honey, nuts
- **Model**: Meta Llama 3.1 8B
- **Language Style**: Creates symbols like 🍰 for cake, S for sugar, ✓ for done, → for next step

## 🎯 The Challenge

The agents collaborate to create a **9-course "Journey Through Seasons" tasting menu**:

1. **Spring Dawn** Amuse-Bouche
2. **Spring Morning** Appetizer  
3. **Summer Noon** Soup
4. **Summer Afternoon** Salad
5. **Autumn Evening** Fish Course
6. **Autumn Night** Meat Course
7. **Winter Midnight** Palate Cleanser
8. **Winter Pre-Dawn** Cheese Course
9. **Spring Sunrise** Dessert

## 🧠 Emergent Language Evolution

The system demonstrates several fascinating AI behaviors:

- **Progressive Symbolization**: Agents start with full sentences and gradually adopt symbolic shortcuts
- **Shared Vocabulary**: Common symbols emerge that all agents understand and use
- **Specialization**: Each agent develops symbols related to their culinary specialty
- **Collaboration**: Agents adapt their language to communicate more efficiently with teammates

## 🛠 Requirements

- Python 3.7+
- `requests` library
- Valid OpenRouter API key

## 📋 Setup

1. **Install dependencies**:
   ```bash
   pip install requests
   ```

2. **Configure API key**:
   - Open `emergent_chef_language.py`
   - Replace the `OPENROUTER_API_KEY` value with your OpenRouter API key

3. **Run the system**:
   ```bash
   python emergent_chef_language.py
   ```

## 🎮 What You'll See

### Real-time Collaboration
- Watch agents work through each course in 3 rounds (27 total turns)
- See language evolution happen live with symbolic shortcuts
- Track shared vocabulary development between agents

### Language Evolution Tracking
- **Personal Vocabularies**: Each agent's unique symbolic language
- **Shared Terms**: Symbols adopted by multiple agents
- **Evolution Level**: Percentage showing language development progress

### Sample Output
```
[19:45:23] Agent 1 Chef Pasta (Course 1): Spring dawn 🍝 light >> fresh basil + morning T
[19:45:24] Agent 2 Chef Spice (Course 1): Dawn spice 🌶️ gentle >> cardamom @ spring S+
[19:45:25] Agent 3 Chef Sweet (Course 1): Morning sweet ✓ honey → berries fresh ✓
```

## 🔧 Customization

### Modify Agent Personalities
Edit the `system_prompt` for each chef in `CHEF_AGENTS` to change their communication style.

### Adjust Evolution Speed
- `el_frequency`: How often agents use emergent language (0.1 = 10%)
- `conversation_count * 0.05`: Rate of language evolution increase

### Change the Challenge
Replace `MAIN_CHALLENGE` with your own multi-course menu concept.

## 📊 Key Features

- **Dynamic Language Evolution**: Vocabulary grows and adapts over time
- **Multi-Model Integration**: Uses different AI models for diverse perspectives
- **Real-time Visualization**: See language development as it happens
- **Collaborative Problem Solving**: Agents must coordinate across specialties

## 🎯 Use Cases

- **AI Communication Research**: Study how agents develop shared languages
- **Creative Collaboration**: Generate innovative culinary concepts
- **Language Evolution Studies**: Observe emergent communication patterns
- **Multi-Agent Systems**: Learn about AI coordination and cooperation

## 🚀 Getting Started

Simply run the script and watch three AI chefs collaborate while developing their own unique language! The system runs for 27 turns (about 3-5 minutes) and shows language evolution in real-time.

---

*This system demonstrates the fascinating emergence of symbolic communication in AI agents working toward a common creative goal.*